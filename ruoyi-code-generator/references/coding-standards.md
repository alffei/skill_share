# RuoYi 代码生成规范参考

## 一、命名规范

### 1.1 表命名规范

| 规则 | 说明 | 示例 |
|------|------|------|
| 前缀规范 | 使用模块名作为前缀 | `sys_user`, `biz_order` |
| 命名风格 | 小写字母 + 下划线分隔 | `product_category` |
| 表注释 | 必须添加中文注释 | `产品分类表` |

### 1.2 字段命名规范

| 规则 | 说明 | 示例 |
|------|------|------|
| 主键 | 表名单数 + `_id` | `user_id`, `order_id` |
| 创建时间 | `create_time` | datetime 类型 |
| 更新时间 | `update_time` | datetime 类型 |
| 创建者 | `create_by` | varchar(64) |
| 更新者 | `update_by` | varchar(64) |
| 备注 | `remark` | varchar(500) |
| 状态 | `status` | char(1): 0=正常, 1=停用 |
| 删除标志 | `del_flag` | char(1): 0=存在, 2=删除 |

### 1.3 Java 命名规范

| 类型 | 规则 | 示例 |
|------|------|------|
| 类名 | 大驼峰，表名去前缀 | `sys_user` → `SysUser` |
| 变量名 | 小驼峰 | `userName`, `createTime` |
| 常量 | 全大写 + 下划线 | `MAX_RETRY_COUNT` |
| 包名 | 全小写 | `com.ruoyi.system` |

---

## 二、数据类型映射

### 2.1 MySQL → Java 类型映射

```
bigint          → Long
int/integer     → Integer
smallint        → Integer
tinyint         → Integer
tinyint(1)      → Boolean (自动识别布尔类型)
varchar/char    → String
text/longtext   → String
datetime        → Date
timestamp       → Date
date            → Date
decimal/numeric → BigDecimal
float           → Float
double          → Double
blob            → byte[]
```

### 2.2 Java → HTML 控件映射

```
String   → input (默认)
String   → textarea (长度 > 500 或字段名含 content/remark)
String   → select (有字典类型)
String   → radio (状态类字段)
Date     → datetime (日期时间选择器)
Long     → input[type=number]
Integer  → input[type=number]
```

---

## 三、权限配置规范

### 3.1 权限标识格式

```
格式: {moduleName}:{businessName}:{操作类型}

操作类型:
- list    查询列表
- query   查询详情
- add     新增
- edit    修改
- remove  删除
- export  导出
```

### 3.2 示例

```java
// 产品管理模块
@PreAuthorize("@ss.hasPermi('product:product:list')")    // 查询
@PreAuthorize("@ss.hasPermi('product:product:query')")   // 详情
@PreAuthorize("@ss.hasPermi('product:product:add')")     // 新增
@PreAuthorize("@ss.hasPermi('product:product:edit')")    // 修改
@PreAuthorize("@ss.hasPermi('product:product:remove')")  // 删除
@PreAuthorize("@ss.hasPermi('product:product:export')")  // 导出
```

---

## 四、目录结构规范

### 4.1 后端目录结构

```
ruoyi-{module}/
└── src/main/java/com/ruoyi/{module}/
    ├── controller/          # 控制器
    │   └── {ClassName}Controller.java
    ├── domain/              # 实体类
    │   └── {ClassName}.java
    ├── mapper/              # Mapper接口
    │   └── {ClassName}Mapper.java
    └── service/             # 服务层
        ├── I{ClassName}Service.java
        └── impl/
            └── {ClassName}ServiceImpl.java

ruoyi-{module}/
└── src/main/resources/
    └── mapper/{module}/
        └── {ClassName}Mapper.xml
```

### 4.2 前端目录结构

```
ruoyi-ui/
└── src/
    ├── api/{moduleName}/     # API接口
    │   └── {businessName}.js
    └── views/{moduleName}/   # 页面组件
        └── {businessName}/
            └── index.vue
```

---

## 五、代码规范

### 5.1 Controller 规范

```java
@RestController
@RequestMapping("/{moduleName}/{businessName}")
public class {ClassName}Controller extends BaseController {
    
    @Autowired
    private I{ClassName}Service {className}Service;
    
    // 1. 查询列表 - GET /list
    // 2. 查询详情 - GET /{id}
    // 3. 新增     - POST
    // 4. 修改     - PUT
    // 5. 删除     - DELETE /{ids}
    // 6. 导出     - POST /export
}
```

### 5.2 Service 规范

```java
public interface I{ClassName}Service {
    // 查询单条
    {ClassName} select{ClassName}By{PkField}({PkType} {pkField});
    
    // 查询列表
    List<{ClassName}> select{ClassName}List({ClassName} {className});
    
    // 新增
    int insert{ClassName}({ClassName} {className});
    
    // 修改
    int update{ClassName}({ClassName} {className});
    
    // 删除单条
    int delete{ClassName}By{PkField}({PkType} {pkField});
    
    // 批量删除
    int delete{ClassName}By{PkField}s({PkType}[] {pkField}s);
}
```

### 5.3 Mapper XML 规范

```xml
<!-- 结果映射 -->
<resultMap type="{ClassName}" id="{ClassName}Result">
    <id property="{pkField}" column="{pk_column}" />
    <result property="{javaField}" column="{column_name}" />
</resultMap>

<!-- 通用查询 SQL 片段 -->
<sql id="select{ClassName}Vo">
    select {字段列表} from {tableName}
</sql>
```

---

## 六、字典配置规范

### 6.1 常用字典类型

| 字典类型 | 说明 | 字典值 |
|---------|------|--------|
| `sys_normal_disable` | 状态 | 0=正常, 1=停用 |
| `sys_yes_no` | 是否 | Y=是, N=否 |
| `sys_show_hide` | 显示隐藏 | 0=显示, 1=隐藏 |
| `sys_notice_type` | 通知类型 | 1=通知, 2=公告 |
| `sys_oper_type` | 操作类型 | 0=其它, 1=新增... |

### 6.2 自定义字典配置

```sql
-- 插入字典类型
INSERT INTO sys_dict_type (dict_name, dict_type, status, create_by, create_time, remark)
VALUES ('产品分类', 'product_category', '0', 'admin', sysdate(), '产品分类字典');

-- 插入字典数据
INSERT INTO sys_dict_data (dict_sort, dict_label, dict_value, dict_type, status, create_by, create_time)
VALUES (1, '电子产品', '1', 'product_category', '0', 'admin', sysdate());
```

---

## 七、注意事项

### 7.1 安全规范

- ✅ 所有接口必须添加权限注解
- ✅ 删除操作必须记录日志
- ✅ 敏感字段不在列表展示
- ❌ 禁止 SQL 注入风险代码
- ❌ 禁止硬编码敏感信息

### 7.2 性能规范

- ✅ 列表查询使用分页
- ✅ 大数据量导出使用异步
- ✅ 避免 N+1 查询问题
- ❌ 禁止在循环中查询数据库

### 7.3 事务规范

- ✅ 主子表操作使用 `@Transactional`
- ✅ 只读操作使用 `@Transactional(readOnly = true)`
- ❌ 禁止事务方法内捕获异常不抛出
