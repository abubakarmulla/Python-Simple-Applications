# Author ABUBAKAR MULLA @always_learning
# ‎Sunday, ‎July ‎04, ‎2021 8:29 PM
# here we use asynchronous programming using (asyncio package(built-in package)),with which we can control the flow of program as well as we can control the time of execution of program as we can slow it as much as we want and
# unlike the synchronous programming(line by line execution i.e sequentially execution of instruction) which we do normally , this asynchronous type of programming allows you to execute in non sequential manner
# this type of programming can be compared as inturrept request sending when we use (await) keyword and giving control to other task(or function in programming) to execute further instructions
# we can observe that whenever 2 or more func use await keyword then suppose execution has reached to all of the func contaioning await then,
# the await of all func will be executed at same time such that whichever the await of a func1 using less delay will transfer the execution to other func2 and if that func2 has more waiting time in await instruction then again,
# the execution will be transferred to func1
# like this asynchronous type of programming works using package(library) **asyncio**...
import asyncio 
async def fectch_data():
	print("Start fetching")
	await asyncio.sleep(6)
	print("done fetching")
	await asyncio.sleep(1)
	return {'number of elements fetched are' : 10}
async def print_numbers():
	await asyncio.sleep(1)
	for x in range(10):
		print(x)
		await asyncio.sleep(0.5)
async def main():
	task1 = asyncio.create_task(fectch_data())
	task2 = asyncio.create_task(print_numbers())
	value = await task1
	print(value)
	await task2
asyncio.run(main())
input()