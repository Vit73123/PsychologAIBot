async def test_1_test(session_pool):
    print("Test!")
    async with session_pool() as session:
        print(f"{session=}")


async def run_db_tests(session_pool):
    await test_1_test(session_pool)
