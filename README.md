<center>

```ascii
                                                                     
   ▄█   ▄█▄              ▄████████              ▄████████            ▄█            
  ███ ▄███▀             ███    ███             ███    ███           ███            
  ███▐██▀               ███    █▀              ███    █▀            ███            
 ▄█████▀               ▄███▄▄▄                ▄███▄▄▄               ███            
▀▀█████▄              ▀▀███▀▀▀               ▀▀███▀▀▀               ███            
  ███▐██▄               ███    █▄              ███    █▄            ███            
  ███ ▀███▄             ███    ███             ███    ███           ███▌    ▄      
  ███   ▀█▀             ██████████             ██████████           █████▄▄██      
  ▀                                                                 ▀              

```
</center>

install → klyde init → klyde config --api-key sk-... → klyde run aider

## Quickstart

```bash
# 1. Install
pip install .

# 2. Initialize in your repo
cd your-project
klyde init

# 3. Configure an API Key
# Anthropic (Default)
klyde config --api-key sk-ant-...

# OR OpenAI
klyde config --openai-key sk-proj-... --model gpt-4o

# OR OpenRouter
klyde config --openrouter-key sk-or-... --model openrouter/auto

# OR Gemini
klyde config --gemini-key AIza... --model gemini-1.5-pro

# OR Groq
klyde config --groq-key gsk_... --model llama3-8b-8192

# 4. Use your agent as normal
klyde run aider
```

Decisions will automatically populate after you make commits. Review flagged contradictions using `klyde review`. Check current status with `klyde status`.
