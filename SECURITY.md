# Security Policy

## Supported Versions

The GNU Radio Delay Calibrator project is committed to providing security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of GNU Radio Delay Calibrator seriously. If you believe you've found a security vulnerability, please follow these steps:

1. **Do not disclose the vulnerability publicly** until it has been addressed by the maintainers.
2. Email the project maintainers directly at [sotrudnic003@gmail.com](spich:sotrudnic003@gmail.com) with details about the vulnerability.
3. Include the following information in your report:
   - A description of the vulnerability and its potential impact
   - Steps to reproduce the vulnerability
   - Any proof-of-concept code or examples
   - Your name/handle (if you wish to be credited)

## What to Expect

When you submit a vulnerability report, you can expect:

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 3 business days.
2. **Verification**: Our team will work to verify the vulnerability and its impact.
3. **Response Plan**: We will develop a plan to address the vulnerability and communicate this with you.
4. **Public Disclosure**: Once the vulnerability is fixed, we will coordinate with you on the public disclosure (if appropriate).

## Security Best Practices for Users

To ensure the security of your GNU Radio Delay Calibrator deployments:

1. **Keep Updated**: Always use the latest version with security patches applied.
2. **Least Privilege**: Run GNU Radio Delay Calibrator with the minimum necessary permissions.
3. **Network Isolation**: When processing sensitive signals, consider network isolation for the system running GNU Radio.
4. **Input Validation**: Be cautious about the source of signal inputs processed by the calibrator.

## Development Practices

Our team follows these security best practices during development:

1. Code reviews with security considerations
2. Regular dependency updates to address known vulnerabilities
3. Static code analysis to identify potential security issues
4. Minimal use of external dependencies

## Third-Party Libraries

GNU Radio Delay Calibrator uses several third-party libraries. While we make efforts to ensure these dependencies are secure, security vulnerabilities may be present in these components. We recommend keeping all system libraries up to date.

---

This security policy may be updated periodically to reflect changes in our security practices and procedures.