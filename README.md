# AdminOps Console (MVP)

## Overview
AdminOps Console is a lightweight internal administration tool designed to
track systems, incidents, changes, and audit activity with role-based access control.

## MVP Scope
- Role-based access control
- System inventory and health tracking
- Incident management with history
- Change management with risk classification
- Immutable audit logging

## Design Decisions
- Append-only audit logs
- No destructive actions in MVP
- Status changes logged instead of overwritten
- Minimal UI prioritizing clarity over polish

## What’s Intentionally Missing
- Notifications
- Role management UI
- Change approval workflows
- Exports and reporting
- Pagination and search

## Security Considerations
- Least privilege RBAC
- Auditable state changes
- No PII in free-text fields

## Future Improvements
See `/docs` for roadmap and threat model.
