First:
- brew install pkg-config cmake
dans le venv: 
- pip install poetry
- brew install pkconfig cmake

In VScode terminal:
- poetry init
'n' pour Author, 'no' for the dependencies
pyproject.toml apparait

download llama cpp source code, and compile it with cmake:
copy the github of ggerganov (type llammacpp github on google)
paste on mistral repo
- cd llamacpp
- make (1 min wait time)
- poetry add torch
- poetry add toechvision
- poetry add huggingface-hub
- cd models

sur google TheBloke/Mistral-7B-v0.1-GGUF
choose model Q4_K_M (6.87 GB)

- cd .. (come back at llamacpp repo)
- ./main -m ./models/mistral-7b-v0.1.Q4_K_M.gguf -t 8 -n 128 -p 'Q: Who was the first man on the moon? '
'-m' is how we pass the model

code model from python to instrument it 
we need new dependencies
google: github lammacpp python (first link, macos installation)
go back to repo mistral
copy 'llama-cpp-python[server]'
do 
- poetry add 'llama-cpp-python[server]'

go down to page to find "high level api"
copy first paragraph to main.py replacing 'path//to/model' by the path of the model
make sure I have the correct interpretor 'poetry' (cmd+shift+p, python: select interpreter)

terminal:
- python3 main.py
