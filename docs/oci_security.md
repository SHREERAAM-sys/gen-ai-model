# OCI Security Services Overview

## Identity and Access Management (IAM)
IAM is a service that controls access to your cloud resources. It enables you to manage users, groups, and the type of access they have to resources. The service provides user and group management, fine-grained access control policies, multi-factor authentication (MFA), and federation with external identity providers.

## Cloud Guard
Cloud Guard is a cloud-native security and compliance service that monitors, identifies, achieves, and maintains the security of your cloud resources. It provides continuous monitoring of cloud resources, automated detection of security issues, and integrated remediation capabilities.

## Security Zones
Security Zones ensure that resources comply with Oracle security principles by enforcing security policies on those resources. The service provides predefined security policies, automatic policy enforcement, and prevents creation of non-compliant resources.

## Vault
Vault is a managed service that enables you to centrally manage and control the lifecycle of keys and secrets used to encrypt and securely access resources and data. It provides centralized key management with Hardware Security Module (HSM) backing and integration with OCI services for encryption.

## Web Application Firewall (WAF)
WAF protects applications from malicious and unwanted internet traffic, helping to improve application security and availability. It provides protection against OWASP Top 10 vulnerabilities, custom security rules, bot management, and API protection.

## Data Safe
Data Safe provides a set of features for protecting sensitive and regulated data in Oracle databases. It includes security assessment, user assessment, data discovery, data masking, and activity auditing capabilities.

## Bastion
Bastion provides restricted and time-limited secure access to resources that don't have public endpoints. It offers temporary, managed SSH access, integration with IAM for access control, and session management and auditing.

## Network Security Groups (NSG)
NSGs act as virtual firewalls for your cloud resources, controlling inbound and outbound traffic at the instance level. They provide fine-grained network access control with stateful packet inspection and integration with other OCI networking features.

## Vulnerability Scanning Service
Vulnerability Scanning Service helps identify security vulnerabilities in your OCI resources, providing recommendations for remediation. It offers automated vulnerability scans, customizable scan schedules, and detailed vulnerability reports.

## Shielded Instances
Shielded Instances provide enhanced security features for virtual machine (VM) instances, protecting them against unauthorized access, malware, and other security threats at the firmware and OS level. They include features like Secure Boot, Measured Boot, and Virtual Trusted Platform Module.

## IAM Single Sign-On (SSO)
Single Sign-On in OCI IAM allows users to access multiple OCI services and applications using a single set of credentials. It supports federation with external identity providers, SAML 2.0 and OAuth 2.0 protocols, and just-in-time user provisioning.

## Container Image Scanning, Signing & Verification
This service provides robust security measures for container images, ensuring the integrity and security of containerized applications from development to deployment. It includes vulnerability scanning, image signing, and signature verification capabilities integrated with OCI Registry.