import asyncio


async def count(num):
    print(f"One from {num}")
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f"Two from {num}")

async def main():
    await asyncio.gather(count(1), count(2), count(3))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed =time.perf_counter() - s
    print(f"file executed in {elapsed:0.2f} seconds.")