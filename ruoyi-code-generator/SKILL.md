---
name: ruoyi-code-generator
description: "基于若依(RuoYi-Vue v3.9.x)框架规范，从数据表定义生成完整 CRUD 代码（Java Domain/Mapper/Service/Controller、MyBatis XML、Vue 2 页面与 API、菜单 SQL）。Use when the user needs to generate RuoYi code, scaffold a CRUD module, create backend and frontend from a database table, or add a new business module to a RuoYi-Vue project."
---

# RuoYi 代码生成器技能

## 目标

根据用户提供的数据表信息（表名、字段定义），按照若依框架规范生成完整 CRUD 代码。

**输出文件：**
- Java 后端：Domain、Mapper、Service、ServiceImpl、Controller
- MyBatis XML 映射文件
- Vue 前端：页面组件 + API 封装
- 菜单初始化 SQL

---

## 输入参数

| 参数 | 必填 | 说明 | 示例 |
|------|------|------|------|
| `tableName` | 是 | 数据库表名 | `sys_product` |
| `tableComment` | 是 | 表注释/功能名称 | `产品管理` |
| `columns` | 是 | 字段列表（含类型、注释） | 见 [references/examples.md](references/examples.md) |
| `packageName` | 否 | 包路径，默认 `com.ruoyi.system` | `com.ruoyi.business` |
| `moduleName` | 否 | 模块名，默认取表前缀后的名称 | `product` |
| `businessName` | 否 | 业务名称，默认取表名去前缀 | `product` |
| `author` | 否 | 作者名，默认 `ruoyi` | `zhangsan` |
| `tplCategory` | 否 | 模板类型: `crud`/`tree`/`sub`，默认 `crud` | `crud` |

---

## 执行流程

### 1. 信息收集与验证

1. 解析用户请求，识别表名与字段信息。
2. 如果缺少必填参数（`tableName`、`tableComment`、`columns`），主动询问用户。
3. 推断默认值：
   - `className` = 表名转大驼峰（去除表前缀如 `sys_`）
   - `moduleName` = 表前缀后的模块名
   - `businessName` = 表名去前缀后的小写形式
   - 主键字段 = `isPk=true` 的字段，默认为 `{tableName}_id`
4. **验证检查点**：向用户确认推断的类名、模块名、包路径是否正确，再继续。

### 2. 变量准备

根据输入计算所有模板变量（`${ClassName}`, `${className}`, `${moduleName}`, `${businessName}`, `${packageName}`, `${permissionPrefix}` 等）。

完整变量清单参见 [references/coding-standards.md](references/coding-standards.md)。

### 3. 代码生成

按顺序读取 `templates/` 目录中的 Velocity 模板并填充：

1. **Java 后端** — `templates/java/*.vm`：Domain → Mapper → Service → ServiceImpl → Controller
2. **MyBatis XML** — `templates/xml/mapper.xml.vm`
3. **Vue 前端** — `templates/vue/index.vue.vm` + `templates/js/api.js.vm`
4. **菜单 SQL** — `templates/sql/sql.vm`

对每个生成文件执行变量替换（`${变量名}` → 实际值）和条件/循环处理（`#if`/`#foreach`）。

### 4. 自检与交付

1. **编译验证**：检查生成的 Java 代码包路径、import 语句、注解是否完整。
2. **安全检查**：确认 Controller 包含 `@PreAuthorize` 权限注解，删除操作包含 `@Log`。
3. **依赖提示**：告知用户需要在 `pom.xml` 或路由配置中添加的内容。
4. **验证检查点**：列出所有生成的文件路径，供用户确认。

---

## 约束条件

**命名规范：**
- 类名：大驼峰 (PascalCase)；变量名：小驼峰 (camelCase)；包路径：全小写

**编码规范：**
- UTF-8 编码，4 空格缩进，完整 Javadoc 注释

**安全规范：**
- Controller 必须添加 `@PreAuthorize` 权限注解
- 删除操作必须添加 `@Log` 日志注解
- 敏感字段（如密码）不出现在列表展示中

**禁止事项：**
- 不生成测试类（如需要请单独请求）
- 不修改已存在的文件（除非用户明确要求）
- 不硬编码任何敏感信息

字段类型映射与编码标准详见 [references/coding-standards.md](references/coding-standards.md)。

---

## 模板引用

| 类别 | 路径 | 说明 |
|------|------|------|
| Java | `templates/java/*.vm` | Domain、Mapper、Service、ServiceImpl、Controller |
| Vue | `templates/vue/index.vue.vm` | 列表页面组件 |
| JS | `templates/js/api.js.vm` | API 封装 |
| XML | `templates/xml/mapper.xml.vm` | MyBatis 映射文件 |
| SQL | `templates/sql/sql.vm` | 菜单初始化 SQL |

---

## 示例

**用户输入：**
```
生成代码:
- 表名: biz_order
- 功能: 订单管理
- 包路径: com.ruoyi.business
- 字段: order_id(bigint,主键), order_no(varchar(50),订单号), customer_name(varchar(100),客户名), amount(decimal(10,2),金额), status(char(1),状态), create_time(datetime,创建时间)
```

**生成结果：**
```
java/domain/Order.java
java/mapper/OrderMapper.java
java/service/IOrderService.java
java/service/impl/OrderServiceImpl.java
java/controller/OrderController.java
xml/OrderMapper.xml
vue/api/order.js
vue/views/order/order/index.vue
sql/orderMenu.sql
```

更多示例见 [references/examples.md](references/examples.md)。

---

## 版本兼容

- **RuoYi-Vue**: v3.9.x
- **前端**: Vue 2 + Element UI
- **后端**: Spring Boot 2.x + MyBatis
