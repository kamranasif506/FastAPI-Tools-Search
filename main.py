from fastapi import FastAPI

app = FastAPI()

# Your dummy search function
def dummy_search_function(user_prompt):
    data = [
        {"tool_name": "Tool 1", "description": f"Description for {user_prompt} - 1", "link": "http://link1.com"},
        {"tool_name": "Tool 2", "description": f"Description for {user_prompt} - 2", "link": "http://link2.com"},
        {"tool_name": "Tool 3", "description": f"Description for {user_prompt} - 3", "link": "http://link3.com"},
        {"tool_name": "Tool 4", "description": f"Description for {user_prompt} - 4", "link": "http://link4.com"},
        {"tool_name": "Tool 5", "description": f"Description for {user_prompt} - 5", "link": "http://link5.com"}
    ]
    return data

# FastAPI endpoint for search
@app.get("/search")
def search_tools(query: str):
    result = dummy_search_function(query)
    return {"results": result}
