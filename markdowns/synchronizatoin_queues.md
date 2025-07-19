### The Role of Each Synchronization Primitive

Think of these tools as different ways for coroutines to coordinate, not all of which involve passing data.

1. asyncio.Event (The Traffic Light)
   Purpose: Simple signaling. It's a binary flag that one coroutine can set (event.set()) to unblock one or more other coroutines that are waiting for it (await event.wait()).
   Data Passing: It does not pass data. When a coroutine is unblocked by an event, it simply resumes execution. It doesn't receive any value. It's like a traffic light turning green—it tells you when to go, but doesn't hand you a package.
2. asyncio.Lock (The Key to a Room)
   Purpose: Mutual exclusion. It ensures that only one coroutine can enter a "critical section" of code at a time.
   Data Passing: It does not pass data directly. Instead, it protects a shared resource (like a list, dictionary, or object) that holds the data. The coroutines communicate by modifying this shared resource, and the lock just prevents them from doing it at the same time and causing corruption. The data is on the "whiteboard inside the room," not passed by the key itself.
3. asyncio.Future (The IOU)
   Purpose: Represents the eventual result of a single, one-time operation.
   Data Passing: It's a one-way, one-time data transfer. A producer coroutine can set a result on the future (future.set_result(value)), and a consumer can await it to get that single value. Once the result is set, the future is "done" and cannot be used to pass more data. It's like an IOU—you hand it over, and eventually, you get a single payment back. You can't use the same IOU for another payment.
   Why Queue and .send() Are Different
   asyncio.Queue (The Conveyor Belt): This is explicitly designed for streaming data. It's a channel where producers can continuously put items and consumers can continuously get them. It's the standard tool for decoupled, many-to-many communication in modern asyncio.
   Generator .send() (The Phone Call): This is the classic method for tightly coupled, two-way communication with a single generator-based coroutine. yield sends data out, and .send() sends data in. It is inherently "back and forth."

### Summary Table

Primitive Purpose Data Flow Analogy
asyncio.Queue Streaming data between tasks Many-to-many, continuous Conveyor Belt
asyncio.Event Simple signaling None (just a signal) Traffic Light
asyncio.Lock Protecting shared state Indirect (via the shared state) Key to a Room
asyncio.Future A single eventual result One-way, one-time IOU / Promise
Generator .send() Two-way communication One-to-one, back and forth Phone Call

### To send data back and forth between multiple workers using async/await

1. asyncio.Queue
2. send(): generators can be used if we use @coroutine type for the async method

### Returning data from a pipeline

That's an excellent and very practical question. You've correctly identified that you can't simply return a value from a long-running asynchronous function or pipeline without stopping it.

Practically this means from an async function running a while True loop, we cannot simply return a value, if we do so,
it will exit the async task and data pipeline will be broken meaning the producer/consumer will stop

To get data out of a running system, you need to establish a communication channel back to the part of your program that needs the data.
