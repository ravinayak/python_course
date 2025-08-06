import asyncio

class CustomAwait:
	def __init__(self, n):
		self.n = n
  
	def __await__(self):
		print('Custom Await Class object await method being called')
		yield
		print('Await method exiting')
        
async def main():
    ca = CustomAwait(20)
    await ca
    
asyncio.run(main())
    