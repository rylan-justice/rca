### Usage
|Classes|Functions|Parameters|
|:-:|:-:|:-:|
|None|`key`|`symbols` `start` `stop`|
|Symmetric|`encrypt` `decrypt`|`plaintext` `ciphertext`|
### Visualization
```mermaid
flowchart LR;V1(Encryption)---V2(Key)-->V3(Plaintext)-->V4(Ciphertext);V5(Decryption)---V6(Key)-->V7(Ciphertext)-->V8(Plaintext)
style V1 fill:#0d1117,stroke:#30363d
style V2 fill:#161b22,stroke:#30363d
style V3 fill:#0d1117,stroke:#30363d
style V4 fill:#161b22,stroke:#30363d
style V5 fill:#0d1117,stroke:#30363d
style V6 fill:#161b22,stroke:#30363d
style V7 fill:#0d1117,stroke:#30363d
style V8 fill:#161b22,stroke:#30363d
```
