### Usage
|Classes|Functions|Parameters|
|:-:|:-:|:-:|
|None|`key`|`symbols` `start` `stop`|
|Symmetric|`encrypt` `decrypt`|`plaintext` `ciphertext`|
### Visualization
```mermaid
flowchart LR;1(Symmetric)---2(Encryption)---3(Key)-->4(Plaintext)-->5(Ciphertext);1(Symmetric)---6(Decryption)---7(Key)-->8(Ciphertext)-->9(Plaintext)
style 1 fill:#0d1117,stroke:#30363d
style 2 fill:#161b22,stroke:#30363d
style 3 fill:#0d1117,stroke:#30363d
style 4 fill:#161b22,stroke:#30363d
style 5 fill:#0d1117,stroke:#30363d
style 6 fill:#161b22,stroke:#30363d
style 7 fill:#0d1117,stroke:#30363d
style 8 fill:#161b22,stroke:#30363d
style 9 fill:#0d1117,stroke:#30363d
```
