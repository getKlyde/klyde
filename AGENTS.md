# AGENTS.md

## What this project is
klyd: a CLI tool that wraps coding agents via git hooks to inject architectural memory.

## Stack (frozen — do not deviate)
- Python 3.11+
- Click for CLI
- SQLite via stdlib sqlite3 (no ORM)
- POSIX shell for hook scripts
- Anthropic API (claude-sonnet-4-6) via BYOK

## Module responsibilities (do not blur these)
- cli.py: Click entrypoint only. No business logic.
- db.py: All SQLite operations. Nothing else.
- extractor.py: One function — LLM extraction call. Nothing else.
- injector.py: One function — format injection string. Nothing else.
- hooks.py: Install/uninstall git hooks. Nothing else.

## Hard rules
- Two LLM calls per commit cycle maximum
- No external dependencies beyond Click and anthropic SDK
- Every function does one thing
- Shell hooks are dumb — they call klyd CLI, contain no logic themselves
- Never add a dependency to solve a problem that stdlib solves

```ascii                                                                                   
                                                                                                   
8 8888     ,88'           8 8888                   `8.`8888.      ,8'           8 888888888o.      
8 8888    ,88'            8 8888                    `8.`8888.    ,8'            8 8888    `^888.   
8 8888   ,88'             8 8888                     `8.`8888.  ,8'             8 8888        `88. 
8 8888  ,88'              8 8888                      `8.`8888.,8'              8 8888         `88 
8 8888 ,88'               8 8888                       `8.`88888'               8 8888          88 
8 8888 88'                8 8888                        `8. 8888                8 8888          88 
8 888888<                 8 8888                         `8 8888                8 8888         ,88 
8 8888 `Y8.               8 8888                          8 8888                8 8888        ,88' 
8 8888   `Y8.             8 8888                          8 8888                8 8888    ,o88P'   
8 8888     `Y8.           8 888888888888                  8 8888                8 888888888P'      

```

---

```ascii

888  /         888           Y88b    /       888~-_   
888 /          888            Y88b  /        888   \  
888/\          888             Y88b/         888    | 
888  \         888              Y8Y          888    | 
888   \        888               Y           888   /  
888    \       888____          /            888_-~   
                                                                                      
```

---

```ascii
 __   ___       _______       _______      ___       
|/"| /  ")     /"     "|     /"     "|    |"  |      
(: |/   /     (: ______)    (: ______)    ||  |      
|    __/       \/    |       \/    |      |:  |      
(// _  \       // ___)_      // ___)_      \  |___   
|: | \  \     (:      "|    (:      "|    ( \_|:  \  
(__|  \__)     \_______)     \_______)     \_______)                                                   

```

---

```ascii

'||'  |'     '||'         '||' '|'    '||''|.   
 || .'        ||            || |       ||   ||  
 ||'|.        ||             ||        ||    || 
 ||  ||       ||             ||        ||    || 
.||.  ||.    .||.....|      .||.      .||...|'  
                                                                                             
```
