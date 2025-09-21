
import uuid
from contextvars import ContextVar

from starlette.requests import Request

request_id:ContextVar[str] = ContextVar('request_id',default='')   #请求ID

class TraceID:
    @staticmethod
    def set(req_id:str)->ContextVar[str]:
        if not req_id:
            req_id = uuid.uuid4().hex
        request_id.set(req_id)
        return  request_id

# 配置 logger 时使用 patcher
def add_request_id(record):
    try:
        record["extra"]["request_id"] = request_id.get()
    except LookupError:
        record["extra"]["request_id"] = None


async def add_request_id_middleware(request: Request, call_next):
    # 为每个请求生成一个唯一的 request_id
    req_id = str(uuid.uuid4())

    # 设置 ContextVar 的值
    request_id_token = request_id.set(req_id)

    try:
        response = await call_next(request)
        # 你可以选择将 request_id 添加到响应头中
        response.headers['request_id'] = req_id
        return response
    finally:
        # 清理 ContextVar，确保上下文管理正确
        request_id.reset(request_id_token)
