package com.example.pokeapi;

import java.time.LocalDateTime;
//Used to get the current date and time
import java.util.HashMap;
import java.util.Map;
//Map → stores key–value pairs
//HashMap → implementation of Map
import java.util.concurrent.atomic.AtomicInteger;
//Used to count total HTTP requests safely
//A thread-safe counter
//Used to count total HTTP requests safely
import org.springframework.boot.SpringApplication;
//@SpringBootApplication= @configure + @Enableautoconfigration + @componentscan
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
//The part after /pokemon/, /echo/, or /user/ changes every request.
//@PathVariable captures that changing value.
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class PokeapiApplication {

    private final AtomicInteger requestCount = new AtomicInteger(0);
    private final LocalDateTime startTime = LocalDateTime.now();
    //private means:This variable can be accessed only inside this class.
    //final means:The variable cannot be reassigned after it is initialized.

    public static void main(String[] args) {
        SpringApplication.run(PokeapiApplication.class, args);
    }

    @GetMapping("/")
    public Map<String, Object> home() {
        requestCount.incrementAndGet();

        Map<String, Object> response = new HashMap<>();
        response.put("service", "PokéAPI");
        response.put("status", "running");
        response.put("environment", "AWS EC2");
        response.put("time", LocalDateTime.now());

        return response;
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        requestCount.incrementAndGet();
        return Map.of("health", "UP");
    }

    @GetMapping("/ping")
    public Map<String, String> ping() {
        requestCount.incrementAndGet();
        return Map.of("response", "pong");
    }

    @GetMapping("/time")
    public Map<String, Object> time() {
        requestCount.incrementAndGet();
        return Map.of(
            "serverTime", LocalDateTime.now(),
            "timezone", "Server Local Time"
        );
    }

    @GetMapping("/echo/{message}")
    public Map<String, String> echo(@PathVariable String message) {
        requestCount.incrementAndGet();
        return Map.of("echo", message);
    }

    @GetMapping("/pokemon/{name}")
    public Map<String, String> pokemon(@PathVariable String name) {
        requestCount.incrementAndGet();
        return Map.of(
            "pokemon", name,
            "message", "Pokémon selected successfully"
        );
    }

    @GetMapping("/status")
    public Map<String, Object> status() {
        return Map.of(
            "startedAt", startTime,
            "currentTime", LocalDateTime.now(),
            "totalRequests", requestCount.get()
        );
    }
}

//git status
//git add filename1 filename2
//git commit 
//git push origin main