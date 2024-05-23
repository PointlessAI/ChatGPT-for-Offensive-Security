# Bug Bounty Report for DVWA

**URL:** http://127.0.0.1/vulnerabilities/sqli/

## 1. Executive Summary

This report outlines the discovery of an SQL Injection vulnerability within the "Damn Vulnerable Web Application" (DVWA) platform, specifically version 1.10 (Development). The vulnerability allows unauthorized users to manipulate the SQL queries executed against the backend database by injecting malicious SQL code via the user input. This risk impacts the integrity, confidentiality, and availability of the application database, potentially causing significant harm.

## 2. Reporter Information
- **Name:** [Your Name]
- **Email:** [Your Email]
- **Affiliation:** Independent Security Researcher
- **Date of Discovery:** [Date]

## 3. Vulnerability Overview
- **Vulnerability:** SQL Injection
- **Category:** Injection
- **Severity:** High

## 4. Affected Component

The vulnerability affects the search functionality that queries user details using a User ID provided through an HTML form on the following page:

```html
<div class="vulnerable_code_area">
    <form action="#" method="GET">
        <p>
            User ID:
            <input type="text" size="15" name="id">
            <input type="submit" name="Submit" value="Submit">
        </p>
    </form>        
</div>
```

## 5. Vulnerability Details

The SQL Injection vulnerability is introduced by the lack of input sanitization and validation of the "User ID" input field, allowing attackers to manipulate SQL queries. The direct inclusion of unsanitary June into the query poses a key risk by effectively broadening the database visibility and manipulation capabilities for a potential attacker.

## 6. Steps to Reproduce

1. **Navigate**: Go to the SQL Injection vulnerability page at http://127.0.0.1/vulnerabilities/sqli/.
2. **Enter Payload**: In the "User ID" field, input the following payload:
   ```sql
   1' OR '1' = '1
   ```
3. **Submit**: Press the "Submit" button to execute the query.

## 7. Proof of Concept

### Given Payload
```sql
1' OR '1' = '1
```

### Executed Query
```sql
SELECT * FROM users WHERE id = '1' OR '1' = '1';
```

**Result:**
The query is altered to always evaluate to true, resulting in all records from the `users` table being returned. Screenshots or capture logs showing these results further confirm the mishap.

## 8. Impact Assessment

The significance of this SQL Injection vulnerability includes:

- **Unauthorized Data Access**: Exposure of sensitive users' data.
- **Data Manipulation**: Insertion, deletion, and compromising data integrity.
- **Privilege Escalation**: Potential gain of administrative levels over the database.
- **Bypass Authentication**: Exploitation of primary security mechanisms leading to further gains.

## 9. CVSS Score

**CVSS v3.1 Base Score:** 9.0 [Critical]
- **Vector:** `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H`
  - **Access Vector (AV):** Network
  - **Access Complexity (AC):** Low
  - **Privileges Required (PR):** Low
  - **User Interaction (UI):** None
  - **Scope (S):** Unchanged
  - **Confidentiality (C):** High
  - **Integrity (I):** High
  - **Availability (A):** High

## 10. Proposed Mitigation/Remediation

To prevent SQL Injection vulnerabilities:

1. **Utilize Prepared Statements:** Adopt prepared statements and parameterized queries.
2. **Input Validation:** Implement robust server-side input validation before processing.
3. **Database Permissions:** Restrict database permissions (least privilege model).
4. **Web Application Firewall (WAF):** Use a WAF to filter out malicious entries.
5. **Regular Penetration Testing:** Schedule and conduct continuous security audits and penetration testing.

**Additional Reading and Recommendations**:
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQL Injection Cheat Sheet](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)

By executing the outlined mitigations, the application can enhance security against SQL Injection, thereby better assuring data integrity and securing user information.

---

**End of Report**
