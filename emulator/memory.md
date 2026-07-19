# i have to add this in future

| Address | Name      | Description                                                    |
| ------: | --------- | -------------------------------------------------------------- |
|   `246` | `RNG`     | Read-only. Returns a random byte (`0-255`) each read.          |
|   `247` | `KEY0`    | Keyboard state. Bits represent `Z 1 2 3 4 5 6 7`.              |
|   `248` | `KEY1`    | Keyboard state. Bits represent `8 9 Q W E R T Y`.              |
|   `249` | `KEY2`    | Keyboard state. Bits represent `U I O P A S D F`.              |
|   `250` | `KEY3`    | Keyboard state. Bits represent `G H J K L Z X C`.              |
|   `251` | `KEY4`    | Keyboard state. Bits represent `V B N M , . / ;`.              |
|   `252` | `KEY5`    | Keyboard state. Bits represent `← → ↑ ↓ Space Ctrl Shift Alt`. |
|   `253` | `TIME`    | Low 8 bits of Unix time (seconds since epoch).                 |
|   `254` | `MOUSE_X` | Mouse X position (`0-255`).                                    |
|   `255` | `MOUSE_Y` | Mouse Y position (`0-255`).                                    |
