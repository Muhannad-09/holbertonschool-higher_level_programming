# ✅ Task 0: Basics of HTTP/HTTPS

## 🔐 1. Differences Between HTTP and HTTPS

| Feature              | HTTP                                           | HTTPS                                               |
|----------------------|------------------------------------------------|----------------------------------------------------|
| **Full Form**         | HyperText Transfer Protocol                     | HyperText Transfer Protocol Secure                   |
| **Encryption**        | ❌ No encryption; data sent as plain text      | ✅ Encrypted using SSL/TLS                           |
| **Port**              | 80                                             | 443                                                |
| **Certificate**       | ❌ No certificate required                      | ✅ Requires an SSL/TLS certificate from a CA         |
| **Security**          | Vulnerable to interception and tampering       | Secures against man-in-the-middle attacks            |
| **URL Prefix**        | `http://`                                      | `https://`                                           |
| **Use Cases**         | Non-sensitive websites                          | Secure logins, payments, personal data transfers     |

> 🔎 **Note**: The “S” in HTTPS stands for **Secure**.

---

## 🧱 2. Structure of HTTP Requests and Responses

### 🔸 HTTP Request Example:

**Components**:
- **Method**: `GET` – What action to perform
- **Path**: `/index.html` – What resource to fetch
- **Version**: `HTTP/1.1` – Protocol version
- **Headers**: Metadata about the request (e.g., User-Agent, Accept)
- **Body**: Only in methods like POST, PUT (not shown here)

Example HTTP Request:


