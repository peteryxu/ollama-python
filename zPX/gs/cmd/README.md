#

## BLOG
https://ollama.com/blog

## IBM Granite
https://ollama.com/blog/ibm-granite


## CLI CMD to run

- ollama run llama3.2-vision "describe this image: /Users/peter/CODE/oss/ollama/img/ivlogo.png" 
- ollama run llama3.2-vision "describe this image: /Users/peter/CODE/_demoData/imgs/hand_drawing.png" 


## CURL using API
- curl http://localhost:11434/api/embeddings -d '{
  "model": "mxbai-embed-large",
  "prompt": "Llamas are members of the camelid family"
}'
- curl http://localhost:11434/api/embeddings -d '{
  "model": "granite-embedding:278m",
  "prompt": "Llamas are members of the camelid family"
}'