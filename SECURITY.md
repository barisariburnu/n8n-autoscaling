# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.x.x   | :white_check_mark: |
| 1.x.x   | :x:                |

## Reporting a Vulnerability

We take the security of n8n-autoscaling seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please Do Not

- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it has been addressed

### Please Do

1. **Email us directly** at the maintainer's email or create a private security advisory on GitHub
2. **Provide detailed information** about the vulnerability:
   - Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
   - Full paths of source file(s) related to the manifestation of the issue
   - The location of the affected source code (tag/branch/commit or direct URL)
   - Any special configuration required to reproduce the issue
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the issue, including how an attacker might exploit it

### What to Expect

- **Acknowledgment**: We will acknowledge your email within 48 hours
- **Communication**: We will keep you informed about our progress
- **Fix Timeline**: We aim to release a fix within 30 days for critical vulnerabilities
- **Credit**: We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Best Practices

When deploying n8n-autoscaling, please follow these security best practices:

### 1. Environment Variables

- **Never commit `.env` files** to version control
- **Use strong passwords** for all services (PostgreSQL, Redis, n8n)
- **Generate unique encryption keys** (N8N_ENCRYPTION_KEY should be 32 characters)
- **Rotate credentials regularly**

### 2. Network Security

- **Use Cloudflare Tunnel** or similar secure tunneling solutions
- **Don't expose Redis or PostgreSQL ports** to the internet
- **Use Tailscale or VPN** for administrative database access
- **Enable firewall rules** to restrict access

### 3. Docker Security

- **Keep Docker updated** to the latest stable version
- **Use Docker socket carefully** - the autoscaler needs access but limit exposure
- **Run containers as non-root** where possible
- **Scan images for vulnerabilities** regularly

### 4. Application Security

- **Keep n8n updated** to the latest version
- **Review workflow permissions** carefully
- **Limit external module access** (NODE_FUNCTION_ALLOW_EXTERNAL)
- **Enable HTTPS** for all external access
- **Use secure cookies** in production (N8N_SECURE_COOKIE=true)

### 5. Database Security

- **Use strong PostgreSQL passwords**
- **Enable SSL/TLS for database connections** in production
- **Regular backups** with encryption
- **Limit database user permissions** to minimum required

### 6. Redis Security

- **Set a Redis password** in production
- **Disable dangerous commands** if not needed
- **Use Redis ACLs** for fine-grained access control
- **Keep Redis updated**

### 7. Monitoring and Logging

- **Monitor logs** for suspicious activity
- **Set up alerts** for unusual scaling patterns
- **Review access logs** regularly
- **Keep logs secure** and rotate them appropriately

## Known Security Considerations

### Docker Socket Access

The autoscaler requires access to the Docker socket (`/var/run/docker.sock`) to manage containers. This is a powerful permission that effectively grants root access to the host system. 

**Mitigations:**
- Run autoscaler in an isolated network
- Use Docker socket proxy if needed
- Monitor autoscaler logs for unexpected behavior
- Keep the autoscaler image updated

### Environment Variables in Logs

Be careful when reviewing logs as some commands may expose environment variables. The autoscaler is designed to minimize this, but always review logs before sharing publicly.

### Secrets Management

For production deployments, consider using:
- Docker Secrets
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Or similar secrets management solutions

## Update Process

When a security vulnerability is identified and fixed:

1. A security advisory will be published on GitHub
2. A new version will be released with the fix
3. The CHANGELOG will be updated with security fix details
4. Users will be notified through GitHub releases

## Security Tools

We recommend using these tools to scan for vulnerabilities:

- **Trivy**: For Docker image scanning
- **OWASP Dependency-Check**: For dependency vulnerabilities
- **git-secrets**: To prevent committing secrets
- **Docker Bench**: For Docker security best practices

## Disclaimer

While we strive to make n8n-autoscaling as secure as possible, no system is 100% secure. Use this software at your own risk and always follow security best practices for your specific environment.

## Contact

For security-related questions or concerns, please reach out through:
- GitHub Security Advisories
- GitHub Issues (for non-sensitive security questions)

---

**Last Updated**: 2025-11-26
