from aiogram import Router

from .users.start import router as start_router
from .users.help import router as help_router
from .users.commandHandlers import router as command_handlers
from .users.echo import router as echo_router
from .users.registerHandlers import router as register_handlers
from .users.file_download import router as file_handlers
from .users.send_file_handlers import router as send_file_handlers
from .users.file_id_handler import file_router as file_id_handler
from .users.inline_mode_handler import inline_router as inline_handler
from .users.inline_mode_file_id_handler import inline_router as inline_router_file_id_handler
from .groups.group_handler import group_router
from .channels.channel_handler import channel_router

router = Router()
router.include_router(inline_router_file_id_handler)
# router.include_router(inline_handler)
router.include_router(register_handlers)
router.include_router(start_router)
router.include_router(help_router)

router.include_router(group_router)
router.include_router(channel_router)

router.include_router(command_handlers)
router.include_router(file_id_handler)
router.include_router(file_handlers)
router.include_router(send_file_handlers)
router.include_router(echo_router)



