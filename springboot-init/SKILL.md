---
name: springboot-init
description: “Scaffolds a Spring Boot 3.x monolithic project with enforced layered architecture — generates directory structure, pom.xml, application.yml, and base classes (BaseResponse, GlobalExceptionHandler, MybatisPlusConfig), enforces strict DTO/VO/Entity data flow, and provides module creation workflows with naming conventions. Use when setting up a new Spring Boot project, initializing a Java backend, scaffolding a Maven project with MyBatis-Plus, configuring Spring Boot 3.x dependencies, or adding a new CRUD module to an existing Spring Boot monolith.”
---

# springboot-init

## 目录
1. [技术栈](#1-技术栈配置) | 2. [项目结构](#2-项目结构与分层) | 3. [编码规范](#3-编码规范) | 4. [统一响应/异常](#4-统一响应与异常)
5. [访问控制/工具](#5-访问控制--工具库) | 6. [命名规范](#6-命名规范) | 7. [执行工作流](#7-执行工作流) | 8. [禁止事项](#8-禁止事项) | 9. [代码模板](#9-代码模板)

---

## 1. 技术栈配置

| 配置项 | 推荐选型 | 说明 |
|--------|---------|------|
| **JDK** | 17 / 21 | Spring Boot 3.x 必须 17+ |
| **ORM** | **MyBatis-Plus** (MP) | 默认选型，快速开发。追求极致性能选 Flex |
| **工具库** | **Hutool** / Guava | 减少重复轮子，增强开发效率 |
| **权限** | **Sa-Token** / Security | 快速开发选 Sa-Token，复杂企业级选 Security |

---

## 2. 项目结构与分层

### 2.1 核心分层
- **manager**: 仅当涉及”跨模块协调”或”第三方集成（OSS/短信）”时启用，避免直接耦合。
- **common/config**: 存放 `BaseResponse`, `GlobalExceptionHandler`, `MybatisPlusConfig` 等。

### 2.2 数据流向（严格执行）

```
Controller ──DTO(Request)──▶ Service ──Entity──▶ Mapper/DB
Controller ◀──VO────────── Service ◀──Entity──── Mapper/DB
```

- **DTO** (Request): `Controller` 输入专用。
- **VO**: `Controller` 输出专用。**严禁**将 `Entity` 直接返回前端。
- **Entity**: 与数据库表一一对应，仅在 `Service/Mapper` 层流通。

---

## 3. 编码规范

### 3.1 Controller & Service
- **返回类型**：强制使用 `BaseResponse<T>`。
- **参数校验**：多参数封装为对象，使用 `@RequestBody` + `Validation`。
- **Service**：业务逻辑收敛于此。MP 风格：`extends ServiceImpl<Mapper, Entity> implements Service`。

### 3.2 Model (Entity/DTO/VO)
- **强制实现**：`Serializable` 并声明 `serialVersionUID`。
- **Java 17+**：优先使用 `record` 定义 DTO/VO。
- **MP 注解**：`@TableName`, `@TableId(type = IdType.ASSIGN_ID)`, `@TableLogic`。

---

## 4. 统一响应与异常

- **ResultUtils**: 提供 `success(data)`, `error(errorCode, msg)`。
- **BusinessException**: 业务逻辑错误必须抛出此异常，由 `GlobalExceptionHandler` 统一捕获。
- **ErrorCode**: 维护全局状态码（如 40000 参数错误、40100 未登录）。

---

## 5. 访问控制 & 工具库

### 5.1 认证方案
- **Sa-Token**: 拦截器校验 `StpUtil.checkLogin()` 或 `@SaCheckRole`。
- **Spring Security**: `SecurityFilterChain` 配置及 `@PreAuthorize`。

### 5.2 工具类推荐 (Hutool)
- `StrUtil.isBlank`, `BeanUtil.copyProperties`, `JSONUtil.toJsonStr`, `SecureUtil.md5`。

---

## 6. 命名规范

| 类型 | 模式 | 示例 |
|------|------|------|
| Controller | `XxxController` | `UserController` |
| Service | `XxxService/Impl` | `UserServiceImpl` |
| DTO | `XxxAdd/Update/QueryRequest` | `UserQueryRequest` |
| VO | `XxxVO` | `UserVO` |
| DAO | `XxxMapper` | `UserMapper` |

---

## 7. 执行工作流

### 7.1 项目初始化

1. **确认配置**：向用户确认 `company`（groupId）、`project`（artifactId）、`jdk` 版本。
2. **生成骨架**：创建目录树，生成 `pom.xml`、`application.yml`。
3. **注入基础类**：生成 `common`、`exception`、`utils`、`config` 包内容（参见 [references/code-templates.md](references/code-templates.md)）。
4. **验证检查点**：运行 `mvn compile`，确认骨架编译通过且无警告。

### 7.2 模块新增

1. **建模**：创建 Entity → Mapper → Service（含 `ServiceImpl`）。
2. **业务端点**：定义 Request/VO（使用 `record`） → Controller 逻辑。
3. **接口文档**：补充 Swagger/OpenAPI 注解。
4. **验证检查点**：运行 `mvn compile` 并测试端点：
   ```bash
   curl -X POST http://localhost:8080/api/<module>/list \
     -H “Content-Type: application/json” \
     -d '{“current”: 1, “pageSize”: 10}'
   ```

### 7.3 Controller 示例

```java
@RestController
@RequestMapping(“/api/user”)
public class UserController {
    @Resource
    private UserService userService;

    @PostMapping(“/list”)
    public BaseResponse<Page<UserVO>> listUsers(@RequestBody UserQueryRequest request) {
        Page<UserVO> page = userService.listUsers(request);
        return ResultUtils.success(page);
    }
}
```

---

## 8. 禁止事项

1. **禁止** 在 Controller 编写任何业务逻辑。
2. **禁止** Entity 跨过 Service 直接暴露给 Controller。
3. **禁止** 未经统一异常处理直接抛出原始 `Exception`。
4. **禁止** 硬编码角色或权限字符串。

---

## 9. 代码模板

参考 [references/code-templates.md](references/code-templates.md)，包含：
`BaseResponse`, `ErrorCode`, `BusinessException`, `GlobalExceptionHandler`, `ResultUtils`, `ThrowUtils`, `MybatisPlusConfig`, `JsonConfig`, `OpenApiConfig`。
