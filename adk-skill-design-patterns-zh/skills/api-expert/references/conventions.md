# FastAPI Conventions

## Route Definitions
- Use `Annotated` for all dependency injection: `user: Annotated[User, Depends(get_user)]`
- Always specify `response_model` on routes returning data
- Use `status_code` parameter: `@app.post("/items", status_code=201)`
- Group related routes with `APIRouter` and `tags`

## Pydantic Models
- Always add `model_config = ConfigDict(from_attributes=True)` for ORM models
- Use `Field()` for validation: `name: str = Field(min_length=1, max_length=100)`
- Separate request models from response models (never expose internal fields)
- Use `Annotated` types for reusable validation: `PositiveInt = Annotated[int, Field(gt=0)]`

## Error Handling
- Raise `HTTPException` with specific status codes, never generic 500
- Use custom exception handlers for domain errors
- Always include `detail` with actionable error messages

## Async vs Sync
- Use `async def` for I/O-bound routes (database, HTTP calls)
- Use plain `def` for CPU-bound routes (FastAPI runs them in a thread pool)
- Never mix `async def` with blocking calls — use `run_in_executor`

## Dependencies
- Use `Depends()` for shared logic (auth, DB sessions, rate limiting)
- Dependencies can be nested — use this for layered validation
- Use `yield` dependencies for cleanup (DB session close, file cleanup)

## Security
- Never store secrets in code — use environment variables
- Use `OAuth2PasswordBearer` for token-based auth
- Always validate and sanitize path/query parameters
