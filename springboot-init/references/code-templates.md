---

## build 工具

### pom.xml (Maven)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.{company}</groupId>
    <artifactId>{project}</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>{project}</name>
    <description>Spring Boot Project initialized by Agent Skill</description>

    <properties>
        <java.version>17</java.version>
        <mybatis-plus.version>3.5.5</mybatis-plus.version>
        <hutool.version>5.8.25</hutool.version>
        <springdoc.version>2.3.0</springdoc.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-aop</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>3.0.3</version>
        </dependency>
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>${springdoc.version}</version>
        </dependency>
        <dependency>
            <groupId>cn.hutool</groupId>
            <artifactId>hutool-all</artifactId>
            <version>${hutool.version}</version>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

---

## 配置文件

### application.yml

```yaml
server:
  port: 8080
  servlet:
    context-path: /api

spring:
  application:
    name: {project}
  profiles:
    active: dev
  jackson:
    date-format: yyyy-MM-dd HH:mm:ss
    time-zone: GMT+8
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/{project}?useUnicode=true&characterEncoding=UTF-8&useSSL=false
    username: root
    password: {password}

mybatis-plus:
  configuration:
    map-underscore-to-camel-case: true
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
  global-config:
    db-config:
      logic-delete-field: is_delete
      logic-delete-value: 1
      logic-not-delete-value: 0
      id-type: assign_id

springdoc:
  swagger-ui:
    path: /swagger-ui.html
    tags-sorter: alpha
    operations-sorter: alpha
  api-docs:
    path: /v3/api-docs
```

---

## common 包

### BaseResponse.java

```java
package com.{company}.{project}.common;

import com.{company}.{project}.exception.ErrorCode;
import lombok.Data;

import java.io.Serializable;

@Data
public class BaseResponse<T> implements Serializable {
    private int code;
    private T data;
    private String message;

    public BaseResponse(int code, T data, String message) {
        this.code = code;
        this.data = data;
        this.message = message;
    }

    public BaseResponse(T data, int code) {
        this.data = data;
        this.code = code;
    }

    public BaseResponse(ErrorCode errorCode) {
        this(errorCode.getCode(), null, errorCode.getMessage());
    }
}
```

### PageRequest.java

```java
package com.{company}.{project}.common;

import lombok.Data;

@Data
public class PageRequest {
    private int current = 1;
    private int pageSize = 10;
    private String sortField;
    private String sortOrder = "descend";
}
```

### DeleteRequest.java

```java
package com.{company}.{project}.common;

import lombok.Data;

import java.io.Serializable;

@Data
public class DeleteRequest implements Serializable {
    private Long id;
    private static final long serialVersionUID = 1L;
}
```

---

## controller 包

### MainController.java

系统健康检查接口。

```java
package com.{company}.{project}.controller;

import com.{company}.{project}.common.BaseResponse;
import com.{company}.{project}.utils.ResultUtils;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Tag(name = "MainController", description = "系统接口")
@RestController
@RequestMapping("/")
public class MainController {

    /**
     * 健康检查
     *
     * @return
     */
    @GetMapping("/health")
    @Operation(summary = "健康检查")
    public BaseResponse<String> health() {
        return ResultUtils.success("ok");
    }

    /**
     * 初始化检查（用于集成验证）
     */
    @GetMapping("/init-check")
    @Operation(summary = "初始化检查")
    public BaseResponse<String> initCheck() {
        return ResultUtils.success("SpringBoot Project Initialized Successfully!");
    }
}
```

---

## exception 包

### ErrorCode.java

```java
package com.{company}.{project}.exception;

import lombok.Getter;

@Getter
public enum ErrorCode {
    SUCCESS(0, "ok"),
    PARAMS_ERROR(40000, "请求参数错误"),
    NOT_LOGIN_ERROR(40100, "未登录"),
    NO_AUTH_ERROR(40101, "无权限"),
    NOT_FOUND_ERROR(40400, "请求数据不存在"),
    FORBIDDEN_ERROR(40300, "禁止访问"),
    SYSTEM_ERROR(50000, "系统内部异常"),
    OPERATION_ERROR(50001, "操作失败");

    private final int code;
    private final String message;

    ErrorCode(int code, String message) {
        this.code = code;
        this.message = message;
    }
}
```

### BusinessException.java

```java
package com.{company}.{project}.exception;

import lombok.Getter;

@Getter
public class BusinessException extends RuntimeException {
    private final int code;

    public BusinessException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.code = errorCode.getCode();
    }

    public BusinessException(int code, String message) {
        super(message);
        this.code = code;
    }

    public BusinessException(ErrorCode errorCode, String message) {
        super(message);
        this.code = errorCode.getCode();
    }
}
```

### GlobalExceptionHandler.java

```java
package com.{company}.{project}.exception;

import com.{company}.{project}.common.BaseResponse;
import com.{company}.{project}.utils.ResultUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public BaseResponse<?> businessExceptionHandler(BusinessException e) {
        log.error("BusinessException", e);
        return ResultUtils.error(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(RuntimeException.class)
    public BaseResponse<?> runtimeExceptionHandler(RuntimeException e) {
        log.error("RuntimeException", e);
        return ResultUtils.error(ErrorCode.SYSTEM_ERROR, "系统错误");
    }

    @ExceptionHandler(org.springframework.web.bind.MethodArgumentNotValidException.class)
    public BaseResponse<?> validationExceptionHandler(org.springframework.web.bind.MethodArgumentNotValidException e) {
        String message = e.getBindingResult().getAllErrors().get(0).getDefaultMessage();
        log.error("Validation Error: {}", message);
        return ResultUtils.error(ErrorCode.PARAMS_ERROR, message);
    }
}
```

---

## utils 包

### ResultUtils.java

```java
package com.{company}.{project}.utils;

import com.{company}.{project}.common.BaseResponse;
import com.{company}.{project}.exception.ErrorCode;

public class ResultUtils {

    public static <T> BaseResponse<T> success(T data) {
        return new BaseResponse<>(0, data, "ok");
    }

    public static BaseResponse<?> error(ErrorCode errorCode) {
        return new BaseResponse<>(errorCode);
    }

    public static BaseResponse<?> error(int code, String message) {
        return new BaseResponse<>(code, null, message);
    }

    public static BaseResponse<?> error(ErrorCode errorCode, String message) {
        return new BaseResponse<>(errorCode.getCode(), null, message);
    }
}
```

### ThrowUtils.java

```java
package com.{company}.{project}.utils;

import com.{company}.{project}.exception.BusinessException;
import com.{company}.{project}.exception.ErrorCode;

public class ThrowUtils {

    public static void throwIf(boolean condition, RuntimeException e) {
        if (condition) {
            throw e;
        }
    }

    public static void throwIf(boolean condition, ErrorCode errorCode) {
        throwIf(condition, new BusinessException(errorCode));
    }

    public static void throwIf(boolean condition, ErrorCode errorCode, String message) {
        throwIf(condition, new BusinessException(errorCode, message));
    }
}
```

---

## config 包

### MybatisPlusConfig.java

MyBatis-Plus 分页插件配置，非 MyBatis-Plus 技术栈可跳过。

```java
package com.{company}.{project}.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("com.{company}.{project}.mapper")
public class MybatisPlusConfig {

    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return interceptor;
    }
}
```

### JsonConfig.java

Long 类型序列化配置，解决前端 JS 精度丢失问题。

```java
package com.{company}.{project}.config;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;
import com.fasterxml.jackson.databind.exc.InvalidFormatException;
import com.fasterxml.jackson.databind.module.SimpleModule;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;
import org.springframework.boot.autoconfigure.jackson.Jackson2ObjectMapperBuilderCustomizer;
import org.springframework.boot.jackson.JsonComponent;
import org.springframework.context.annotation.Bean;

import java.io.IOException;

@JsonComponent
public class JsonConfig {

    @Bean
    public Jackson2ObjectMapperBuilderCustomizer jackson2ObjectMapperBuilderCustomizer() {
        return builder -> {
            SimpleModule module = new SimpleModule();
            module.addSerializer(Long.class, ToStringSerializer.instance);
            module.addSerializer(Long.TYPE, ToStringSerializer.instance);
            module.addDeserializer(Long.class, new LongDeserializer());
            module.addDeserializer(Long.TYPE, new LongDeserializer());
            builder.modules(module);
        };
    }

    private static class LongDeserializer extends JsonDeserializer<Long> {
        @Override
        public Long deserialize(JsonParser p, DeserializationContext ctxt) throws IOException {
            if (p.currentToken() == JsonToken.VALUE_NUMBER_INT) {
                return p.getLongValue();
            }
            if (p.currentToken() == JsonToken.VALUE_STRING) {
                String value = p.getText().trim();
                if (value.isEmpty()) {
                    return null;
                }
                try {
                    return Long.parseLong(value);
                } catch (NumberFormatException e) {
                    throw new InvalidFormatException(p, "无效的Long格式", value, Long.class);
                }
            }
            throw ctxt.wrongTokenException(p, Long.class, JsonToken.VALUE_NUMBER_INT,
                    "Long类型仅支持数字或字符串格式");
        }
    }
}
```

### OpenApiConfig.java

SpringDoc OpenAPI 配置。

```java
package com.{company}.{project}.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info().title("API 文档"));
    }
}
```
