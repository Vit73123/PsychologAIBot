from aiogram import Dispatcher


async def register_routers(dispatcher: Dispatcher):
    from handlers.admin.admin import router as admin_admin_router
    from handlers.user.user import router as user_user_router

    dispatcher.include_routers(
        admin_admin_router,
        user_user_router,
    )
