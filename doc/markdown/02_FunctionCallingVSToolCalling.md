# Function calling和Tool Calling的区别

Function Calling是早期ChatGPT的概念，在调用API的时候提供参数functions，但是在一次对话中只能调用一个函数，现在已经过时。
```python
completion = client.chat.completions.create(
model="gpt-4o",
messages=[{"role": "user", "content": user_query}],
functions=functions,
function_call="auto"
)
```
Tool Calling是Function calling的基础上进行增强，可以调用多个函数，同时不仅限于function，参数由functions改成了tools，不过官方文档的标题还是叫做Function calling。
```python
completion = client.chat.completions.create(
model="gpt-4o",
messages=[{"role": "user", "content": user_query}],
tools=tools,
tool_choice="auto",
)
```

> 参考 [Anthropic的官方文档标题Tool use (function calling)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)，个人理解得他们现在在各个大模型中叫法不同，但是本质上是一样的。
>
> 参考 [From Function Calls to Tool Calls: A Comprehensive Guide](https://www.tasking.ai/blog/from-function-calls-to-tool-calls-a-comprehensive-guide)
> <b>Function Calls</b>
>
> Using function_calls, developers could directly interact with the AI to perform functions, but <b>this approach had limitations, especially in handling parallel function calls. For instance, within a single chat completion request, it is not feasible to query multiple stock prices simultaneously, as only one tool function can be called at a time</b>. This method is now marked as deprecated on OpenAI's official website.
> <b>Tool Calls</b>
>
> With the introduction of tool_calls, OpenAI provided a more robust framework enabling more complex integrations and interactions.
> - Parallel Function Calling: This feature <b>allows the model to execute multiple function calls simultaneously</b>. For instance, the model can query the weather in three different locations at once. Each function call is managed independently within the tool_calls array, and responses are handled in parallel, reducing round trips and wait times.
> - Integration Flexibility: The structure of <b>tool_calls is designed to support a wide variety of tools, not limited to functions</b>. This design allows for future expansions and integrations of different tool types, enhancing the model's adaptability and application scope.
