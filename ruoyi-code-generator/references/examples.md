# 代码生成示例

本文档提供了代码生成的完整示例，供 Agent 参考学习。

---

## 示例一：简单 CRUD (产品管理)

### 输入信息

```yaml
tableName: biz_product
tableComment: 产品管理
packageName: com.ruoyi.business
moduleName: business
businessName: product
author: ruoyi

columns:
  - name: product_id
    type: bigint
    comment: 产品ID
    isPk: true
    isIncrement: true
    
  - name: product_name
    type: varchar(100)
    comment: 产品名称
    isRequired: true
    isQuery: true
    htmlType: input
    
  - name: product_code
    type: varchar(50)
    comment: 产品编码
    isRequired: true
    
  - name: price
    type: decimal(10,2)
    comment: 价格
    
  - name: status
    type: char(1)
    comment: 状态（0正常 1停用）
    dictType: sys_normal_disable
    htmlType: radio
    
  - name: create_time
    type: datetime
    comment: 创建时间
```

### 生成结果

#### 1. Product.java (实体类)

```java
package com.ruoyi.business.domain;

import java.math.BigDecimal;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.core.domain.BaseEntity;

/**
 * 产品管理对象 biz_product
 * 
 * @author ruoyi
 * @date 2026-01-27
 */
public class Product extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 产品ID */
    private Long productId;

    /** 产品名称 */
    @Excel(name = "产品名称")
    private String productName;

    /** 产品编码 */
    @Excel(name = "产品编码")
    private String productCode;

    /** 价格 */
    @Excel(name = "价格")
    private BigDecimal price;

    /** 状态（0正常 1停用） */
    @Excel(name = "状态", readConverterExp = "0=正常,1=停用")
    private String status;

    public void setProductId(Long productId) 
    {
        this.productId = productId;
    }

    public Long getProductId() 
    {
        return productId;
    }

    public void setProductName(String productName) 
    {
        this.productName = productName;
    }

    public String getProductName() 
    {
        return productName;
    }

    public void setProductCode(String productCode) 
    {
        this.productCode = productCode;
    }

    public String getProductCode() 
    {
        return productCode;
    }

    public void setPrice(BigDecimal price) 
    {
        this.price = price;
    }

    public BigDecimal getPrice() 
    {
        return price;
    }

    public void setStatus(String status) 
    {
        this.status = status;
    }

    public String getStatus() 
    {
        return status;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("productId", getProductId())
            .append("productName", getProductName())
            .append("productCode", getProductCode())
            .append("price", getPrice())
            .append("status", getStatus())
            .append("createTime", getCreateTime())
            .toString();
    }
}
```

#### 2. ProductController.java (控制器)

```java
package com.ruoyi.business.controller;

import java.util.List;
import javax.servlet.http.HttpServletResponse;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.business.domain.Product;
import com.ruoyi.business.service.IProductService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 产品管理Controller
 * 
 * @author ruoyi
 * @date 2026-01-27
 */
@RestController
@RequestMapping("/business/product")
public class ProductController extends BaseController
{
    @Autowired
    private IProductService productService;

    /**
     * 查询产品管理列表
     */
    @PreAuthorize("@ss.hasPermi('business:product:list')")
    @GetMapping("/list")
    public TableDataInfo list(Product product)
    {
        startPage();
        List<Product> list = productService.selectProductList(product);
        return getDataTable(list);
    }

    /**
     * 导出产品管理列表
     */
    @PreAuthorize("@ss.hasPermi('business:product:export')")
    @Log(title = "产品管理", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, Product product)
    {
        List<Product> list = productService.selectProductList(product);
        ExcelUtil<Product> util = new ExcelUtil<Product>(Product.class);
        util.exportExcel(response, list, "产品管理数据");
    }

    /**
     * 获取产品管理详细信息
     */
    @PreAuthorize("@ss.hasPermi('business:product:query')")
    @GetMapping(value = "/{productId}")
    public AjaxResult getInfo(@PathVariable("productId") Long productId)
    {
        return success(productService.selectProductByProductId(productId));
    }

    /**
     * 新增产品管理
     */
    @PreAuthorize("@ss.hasPermi('business:product:add')")
    @Log(title = "产品管理", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody Product product)
    {
        return toAjax(productService.insertProduct(product));
    }

    /**
     * 修改产品管理
     */
    @PreAuthorize("@ss.hasPermi('business:product:edit')")
    @Log(title = "产品管理", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody Product product)
    {
        return toAjax(productService.updateProduct(product));
    }

    /**
     * 删除产品管理
     */
    @PreAuthorize("@ss.hasPermi('business:product:remove')")
    @Log(title = "产品管理", businessType = BusinessType.DELETE)
	@DeleteMapping("/{productIds}")
    public AjaxResult remove(@PathVariable Long[] productIds)
    {
        return toAjax(productService.deleteProductByProductIds(productIds));
    }
}
```

#### 3. product.js (前端 API)

```javascript
import request from '@/utils/request'

// 查询产品管理列表
export function listProduct(query) {
  return request({
    url: '/business/product/list',
    method: 'get',
    params: query
  })
}

// 查询产品管理详细
export function getProduct(productId) {
  return request({
    url: '/business/product/' + productId,
    method: 'get'
  })
}

// 新增产品管理
export function addProduct(data) {
  return request({
    url: '/business/product',
    method: 'post',
    data: data
  })
}

// 修改产品管理
export function updateProduct(data) {
  return request({
    url: '/business/product',
    method: 'put',
    data: data
  })
}

// 删除产品管理
export function delProduct(productId) {
  return request({
    url: '/business/product/' + productId,
    method: 'delete'
  })
}
```

#### 4. productMenu.sql (菜单SQL)

```sql
-- 菜单 SQL
insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理', '1', '1', 'product', 'business/product/index', 1, 0, 'C', '0', '0', 'business:product:list', '#', 'admin', sysdate(), '', null, '产品管理菜单');

-- 按钮父菜单ID
SELECT @parentId := LAST_INSERT_ID();

-- 按钮 SQL
insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理查询', @parentId, '1',  '#', '', 1, 0, 'F', '0', '0', 'business:product:query', '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理新增', @parentId, '2',  '#', '', 1, 0, 'F', '0', '0', 'business:product:add', '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理修改', @parentId, '3',  '#', '', 1, 0, 'F', '0', '0', 'business:product:edit', '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理删除', @parentId, '4',  '#', '', 1, 0, 'F', '0', '0', 'business:product:remove', '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('产品管理导出', @parentId, '5',  '#', '', 1, 0, 'F', '0', '0', 'business:product:export', '#', 'admin', sysdate(), '', null, '');
```

---

## 示例二：对话式代码生成

### 用户请求

> "帮我创建一个订单管理模块，需要有订单号、客户名称、订单金额、订单状态、创建时间这些字段"

### Agent 分析

1. **解析需求**: 订单管理 CRUD
2. **推断表名**: `biz_order` (业务表，使用 biz 前缀)
3. **推断字段**:
   - `order_id` - 主键
   - `order_no` - 订单号 (varchar)
   - `customer_name` - 客户名称 (varchar)
   - `amount` - 订单金额 (decimal)
   - `status` - 订单状态 (需要自定义字典)
   - `create_time` - 创建时间 (datetime)

4. **询问用户**:
   > 我理解您需要创建订单管理模块，我有几个问题需要确认：
   > 1. 订单状态需要哪些选项？(例如：待支付/已支付/已发货/已完成/已取消)
   > 2. 是否需要关联其他表？(例如订单明细)
   > 3. 包路径使用默认的 `com.ruoyi.business` 还是自定义？

5. **用户回复**:
   > 订单状态就用：待支付、已支付、已发货、已完成、已取消。不需要关联其他表。包路径用默认的就行。

6. **生成代码并交付**

---

## 注意事项

1. **字段类型自动推断**
   - 包含 `id` 且为数字类型 → 主键
   - 名称为 `status` → 状态字段，默认使用字典
   - 名称包含 `time/date` → 日期类型
   - 名称包含 `amount/price/money` → BigDecimal

2. **模板变量替换**
   - `${ClassName}` → 类名大驼峰
   - `${className}` → 类名小驼峰
   - `${tableName}` → 数据库表名
   - `${pkColumn.javaField}` → 主键字段名

3. **代码生成后的操作**
   - 执行菜单 SQL 添加权限
   - 重新登录或刷新权限缓存
   - 检查前端路由配置
