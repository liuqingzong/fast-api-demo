import logging
import sys
import os
from pathlib import Path
from loguru import logger
from core.config import settings

class InterceptHandler(logging.Handler):
    """
    日志拦截处理器：将所有 Python 标准日志重定向到 Loguru （用于处理uvicorn / fastapi 等自带的日志）
    工作原理：
    1. 继承自 logging.Handler
    2. 重写 emit 方法处理日志记录
    3. 将标准库日志转换为 Loguru 格式
    """
    def emit(self, record: logging.LogRecord) -> None:
        # 获取日志级别名称
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 获取调用帧信息
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # 使用 Loguru 记录日志
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging():
    """
    配置日志系统：
    1. 移除 Loguru 默认处理器
    2. 添加自定义处理器，输出到标准输出，设置日志格式和级别
    3. 配置 Python 标准日志系统，使用 InterceptHandler 重定向日志到 Loguru
    """
    # 移除 Loguru 默认处理器
    logger.configure(extra={"request_id": None})
    logger.remove()
    
    # 定义日志格式
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {extra[request_id]} | "
        "<level>{level: <8}</level> | "
        "process [<cyan>{process}</cyan>] | thread [<cyan>{thread}</cyan>] | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )

    # 控制台输出
    logger.add(
        sys.stdout,
        format=log_format,
        level="DEBUG" if settings.LOG_LEVEL.lower() == "debug" else "INFO",
        # enqueue=True, # 启用异步写入
        backtrace=True,  # 显示完整的异常堆栈
        # diagnose=True,  # 显示变量值等诊断信息
        colorize=True,  # 启用颜色
    )

    # 创建日志目录
    log_dir = settings.LOG_FILE_PATH.rsplit("/", 1)[0]
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 文件输出，日志轮转
    logger.add(
        str(Path(log_dir, "log.log")),
        format=log_format,
        level="INFO",
        rotation="10 MB",
        retention="30 days",
        encoding="utf-8",
        enqueue=True,  # 异步写入
        # filter=correlation_id_filter
    )
    logger.add(
        str(Path(log_dir, "error.log")),
        format=log_format,
        level="ERROR",
        rotation="10 MB",
        retention="30 days",
        encoding="utf-8",
        enqueue=True,  # 异步写入
        # filter=correlation_id_filter
    )
    
    # 配置 标准库日志 / 第三方库日志
    logger_name_list = [name for name in logging.root.manager.loggerDict]
    for logger_name in logger_name_list:
        _logger = logging.getLogger(logger_name)
        _logger.setLevel(logging.INFO)
        _logger.handlers = []
        _logger.propagate = False
        _logger.addHandler(InterceptHandler())