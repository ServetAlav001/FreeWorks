package com.firstSpringBoot.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(path = "/api")//ARTIK localhost bunun ile calısır.
public class hello {
    //localhost:8080/api/hello
    @GetMapping(path = "/hello")//BU METHOD İLE ASAGIDAKİ METHOD ARASINDA BİR FARK YOKTUR.FAKAT BU DAHA OKULNAKLIDIR.
    //@RequestMapping(path = "/hello",method = RequestMethod.GET)
    public String sayHello(){
        return "hello world!";
    }
    @DeleteMapping(path = "/delete")
    public String delete(){
        return "data delete";
    }
}
