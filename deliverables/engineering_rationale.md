# Engineering Rationale and Design Decisions

## Overview

This project extends **OpenWebUI version 0.6.5** with additional backend capabilities while maintaining clean architecture and modular design.

The goal of the implementation was to integrate new functionality into an existing production-like codebase without breaking its internal architecture. The implemented features focus on operational visibility and controlled system usage through:

- Offline License Enforcement
- Structured Audit Logging for sensitive operations

The design decisions prioritize maintainability, security, and clear separation of responsibilities across modules.

---

# Architectural Considerations

OpenWebUI already follows a layered structure consisting of:

- routers (API endpoints)
- models (database logic)
- internal services
- configuration modules

When adding new features, the goal was to **extend the existing architecture instead of modifying core components unnecessarily**.

To achieve this, both new features were implemented as **separate modules** that integrate with existing routers.

The key design principle followed was:

**Separation of Concerns**

Each component is responsible for a single clearly defined task.

---

# Offline License Enforcement Mechanism

## Motivation

The assignment requires implementing a licensing system that works in a fully offline environment while preventing trivial bypass.

A simple configuration-based license limit could easily be modified by editing a file. Therefore, a **cryptographic license verification mechanism** was implemented.

---

## Design Approach

The licensing system was implemented inside the module:

```
backend/open_webui/licensing
```

This module contains several components:

- license_loader
- license_validator
- license_service
- cryptographic utilities
- public key

The license file is stored at:

```
backend/config/license.json
```

The application loads this license during system startup.

---

## Digital Signature Validation

To prevent tampering with the license file, the license is protected using an **RSA digital signature**.

The application contains only a **public key**, which is used to verify the signature contained in the license file.

This approach ensures that:

- The license cannot be modified without invalidating the signature
- A valid license can only be produced using the private key
- The system can operate completely offline

This satisfies the requirement that the licensing system must function in an **air-gapped environment**.

---

## Application Lifecycle Integration

License validation occurs during the initialization of the `LicenseService`.

If the license signature is invalid, the application will fail during startup.

This approach ensures that an invalid or tampered license cannot be ignored during runtime.

---

## User Limit Enforcement

The license defines a field:

```
max_users
```

During user signup, the system checks the current number of users against this value.

If the limit is reached, the signup request is rejected.

This enforcement is implemented inside the authentication router, ensuring that user creation always respects the license constraints.

---

# Audit Trail for Sensitive Operations

## Motivation

Operational visibility is important for understanding system activity and diagnosing issues.

Instead of relying on console logging, a structured audit system was implemented that stores important events in the database and exposes them through the application interface.

---

## Architecture

The audit system was implemented using three main components:

Database Model

```
models/audit_logs.py
```

Service Layer

```
audit/audit_service.py
```

API Router

```
routers/audit.py
```

This separation ensures that logging logic is centralized and reusable.

Routers simply call the service when an event occurs.

---

## Database Persistence

Audit logs are stored in a dedicated database table using SQLAlchemy.

Each log entry includes:

- event_type
- actor_id
- actor_email
- target_type
- target_id
- message
- metadata
- timestamp

This structure allows events to be queried, filtered, and reviewed by administrators.

---

## Captured Events

The system records several types of sensitive operations, including:

- user authentication events (login/logout)
- user creation
- role changes
- model configuration updates
- license enforcement violations

These events were selected because they represent meaningful administrative or security-related actions.

---

## Administrator Visibility

The audit logs are accessible through the OpenWebUI interface.

A dedicated **Audit page** was added to the admin panel, allowing administrators to review system activity directly within the application.

This improves usability compared to traditional log files.

---

# Security Considerations

Several security principles guided the implementation.

License Integrity

The use of digital signatures prevents unauthorized modification of the license file.

Access Control

Sensitive endpoints such as audit log retrieval require administrator permissions.

Operational Transparency

Audit logs provide visibility into actions performed by users and administrators.

---

# Maintainability and Modularity

Both new features were designed to remain independent from the core application logic.

Key characteristics include:

- isolated modules
- minimal modifications to existing files
- reusable service components
- clear responsibility boundaries

This ensures that the added features can be maintained or extended without impacting unrelated parts of the system.

---

# Tradeoffs and Design Choices

Several tradeoffs were considered during implementation.

Cryptographic Licensing vs Simple Configuration

Using RSA signatures introduces slightly more complexity but significantly improves security and prevents trivial license bypass.

Database Audit Logs vs File Logging

Storing logs in the database allows structured querying and integration with the web interface, which improves usability.

Minimal Invasive Changes

Instead of heavily modifying the core framework, the design focuses on extending the system through modular additions.

---

# Conclusion

The implemented features demonstrate how additional functionality can be integrated into an existing system while maintaining clean architecture and good engineering practices.

The licensing system ensures controlled system usage even in offline environments, while the audit trail improves operational transparency and administrative oversight.

Both features were implemented with an emphasis on modular design, maintainability, and security.
