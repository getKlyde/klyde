# AGENTS.md

## What this project is
klyde: a CLI tool that wraps coding agents via git hooks to inject architectural memory.

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
- Shell hooks are dumb — they call klyde CLI, contain no logic themselves
- Never add a dependency to solve a problem that stdlib solves

```ascii                                        
                                             
   / ___        ___          ___         //  
  //\ \       //___) )     //___) )     //   
 //  \ \     //           //           //    
//    \ \   ((____       ((____       //     

```

---

```ascii

 ___  __            _______           _______           ___          
|\  \|\  \         |\  ___ \         |\  ___ \         |\  \         
\ \  \/  /|_       \ \   __/|        \ \   __/|        \ \  \        
 \ \   ___  \       \ \  \_|/__       \ \  \_|/__       \ \  \       
  \ \  \\ \  \       \ \  \_|\ \       \ \  \_|\ \       \ \  \____  
   \ \__\\ \__\       \ \_______\       \ \_______\       \ \_______\
    \|__| \|__|        \|_______|        \|_______|        \|_______|
                                                                     
                                                                                                                                      
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

          _____                            _____                            _____                            _____  
         /\    \                          /\    \                          /\    \                          /\    \ 
        /::\____\                        /::\    \                        /::\    \                        /::\____\
       /:::/    /                       /::::\    \                      /::::\    \                      /:::/    /
      /:::/    /                       /::::::\    \                    /::::::\    \                    /:::/    / 
     /:::/    /                       /:::/\:::\    \                  /:::/\:::\    \                  /:::/    /  
    /:::/____/                       /:::/__\:::\    \                /:::/__\:::\    \                /:::/    /   
   /::::\    \                      /::::\   \:::\    \              /::::\   \:::\    \              /:::/    /    
  /::::::\____\________            /::::::\   \:::\    \            /::::::\   \:::\    \            /:::/    /     
 /:::/\:::::::::::\    \          /:::/\:::\   \:::\    \          /:::/\:::\   \:::\    \          /:::/    /      
/:::/  |:::::::::::\____\        /:::/__\:::\   \:::\____\        /:::/__\:::\   \:::\____\        /:::/____/       
\::/   |::|~~~|~~~~~             \:::\   \:::\   \::/    /        \:::\   \:::\   \::/    /        \:::\    \       
 \/____|::|   |                   \:::\   \:::\   \/____/          \:::\   \:::\   \/____/          \:::\    \      
       |::|   |                    \:::\   \:::\    \               \:::\   \:::\    \               \:::\    \     
       |::|   |                     \:::\   \:::\____\               \:::\   \:::\____\               \:::\    \    
       |::|   |                      \:::\   \::/    /                \:::\   \::/    /                \:::\    \   
       |::|   |                       \:::\   \/____/                  \:::\   \/____/                  \:::\    \  
       |::|   |                        \:::\    \                       \:::\    \                       \:::\    \ 
       \::|   |                         \:::\____\                       \:::\____\                       \:::\____\
        \:|   |                          \::/    /                        \::/    /                        \::/    /
         \|___|                           \/____/                          \/____/                          \/____/ 
                                                                                                                    
```
