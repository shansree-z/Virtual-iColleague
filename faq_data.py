FAQ_DATA = [
    # IT Support (30 FAQs)
    {"id": 1, "category": "IT", "keyword": "WiFi", 
     "question": "How to connect to office WiFi?", 
     "answer": "Connect to 'Corp_Secure' network. Username: Your Employee ID, Password: Your system password. For issues, call Ext. 5555."},
    
    {"id": 2, "category": "IT", "keyword": "Password", 
     "question": "How to reset my password?", 
     "answer": "Press Ctrl+Alt+Del → Change Password. Or visit password.company.com. Call IT Helpdesk at Ext. 5555 for assistance."},
    
    {"id": 3, "category": "IT", "keyword": "VPN", 
     "question": "How to setup VPN for remote work?", 
     "answer": "Download AnyConnect VPN client from IT portal. Server: vpn.company.com. Need MFA setup first."},
    
    {"id": 4, "category": "IT", "keyword": "Email", 
     "question": "Email not working on phone?", 
     "answer": "Reconfigure using Outlook app. Server: mail.company.com. Enable MFA. Call Ext. 5555 if issues persist."},
    
    {"id": 5, "category": "IT", "keyword": "Software", 
     "question": "Need Microsoft Office installed?", 
     "answer": "Already installed on company laptops. For activation issues, contact IT at Ext. 5555."},
    
    {"id": 6, "category": "IT", "keyword": "Printer", 
     "question": "Printer not printing?", 
     "answer": "Check network connection. Reinstall drivers from IT portal. For hardware issues, call Ext. 5555."},
    
    {"id": 7, "category": "IT", "keyword": "Laptop", 
     "question": "Laptop hardware issue?", 
     "answer": "Visit Tech Bar on 4th floor (9 AM-6 PM). For urgent issues, call Ext. 6666."},
    
    {"id": 8, "category": "IT", "keyword": "Internet", 
     "question": "Internet slow in office?", 
     "answer": "Report to IT at Ext. 5555. They will check network status and resolve."},
    
    {"id": 9, "category": "IT", "keyword": "Teams", 
     "question": "Microsoft Teams not working?", 
     "answer": "Reinstall Teams app. Clear cache. Call Ext. 5555 for meeting setup help."},
    
    {"id": 10, "category": "IT", "keyword": "Access", 
     "question": "Access denied to system?", 
     "answer": "Contact your manager for access request. Then IT will enable. Call Ext. 5555 after approval."},
    
    # HR (25 FAQs)
    {"id": 31, "category": "HR", "keyword": "Salary", 
     "question": "When is salary credited?", 
     "answer": "Salary processed on 28th of each month. If holiday, credited on previous working day. Contact Finance for delays."},
    
    {"id": 32, "category": "HR", "keyword": "Leave", 
     "question": "How to apply for sick leave?", 
     "answer": "1. Inform manager via email. 2. Apply in HR portal under 'Time Off'. 3. Submit medical certificate if >2 days."},
    
    {"id": 33, "category": "HR", "keyword": "Manager", 
     "question": "Who should I report to?", 
     "answer": "Check Org Chart in HR portal. Your direct reporting manager is assigned during onboarding. HR contact: Ext. 4444."},
    
    {"id": 34, "category": "HR", "keyword": "Insurance", 
     "question": "Health insurance claim process?", 
     "answer": "Submit bills to insurance portal. Cashless at network hospitals. Contact HR Benefits team at Ext. 4444."},
    
    {"id": 35, "category": "HR", "keyword": "Tax", 
     "question": "Income tax saving documents?", 
     "answer": "Submit investment proofs by Jan 31st in payroll portal. Form 16 available from April. Contact Finance for queries."},
    
    # Finance (15 FAQs)
    {"id": 56, "category": "Finance", "keyword": "Expenses", 
     "question": "How to claim travel expenses?", 
     "answer": "Submit bills in Expense tool within 15 days of travel. Attach receipts. Approval from manager required. Contact Ext. 3333."},
    
    {"id": 57, "category": "Finance", "keyword": "Reimbursement", 
     "question": "Reimbursement pending?", 
     "answer": "Processed within 10 working days after approval. Check status in Finance portal. Delays? Call Ext. 3333."},
    
    {"id": 58, "category": "Finance", "keyword": "Advance", 
     "question": "Travel advance request?", 
     "answer": "Submit 2 weeks before travel. Max 80% of estimated cost. Approval from Finance Head required."},
    
    # Admin (15 FAQs)
    {"id": 71, "category": "Admin", "keyword": "ID Card", 
     "question": "Lost my ID card?", 
     "answer": "Immediately report to Security Desk (Ground floor). Temporary pass issued. ₹500 charge for replacement."},
    
    {"id": 72, "category": "Admin", "keyword": "Parking", 
     "question": "Parking space allocation?", 
     "answer": "Submit vehicle details to Facilities (Ext. 1111). Permit issued in 2 days. Assigned parking spots."},
    
    {"id": 73, "category": "Admin", "keyword": "Visitor", 
     "question": "Register external visitor?", 
     "answer": "Submit in Security portal 24 hours before. Visitor pass mandatory. Escort required inside premises."},
    
    {"id": 74, "category": "Admin", "keyword": "Travel", 
     "question": "Book flight for business trip?", 
     "answer": "Contact travel desk at travel@company.com or Ext. 3333. Book economy class only."},
    
    {"id": 75, "category": "Admin", "keyword": "Cab", 
     "question": "Late night cab service?", 
     "answer": "Available after 8 PM. Book through transport app (code: COMPANY2024). Bill to company."},
    
    # Security (10 FAQs)
    {"id": 86, "category": "Security", "keyword": "Emergency", 
     "question": "Emergency contact numbers?", 
     "answer": "Security: Ext. 9999 (24/7), Medical: Ext. 8888, Fire: Ext. 7777, IT Emergency: Ext. 6666"},
    
    {"id": 87, "category": "Security", "keyword": "Report", 
     "question": "Report security incident?", 
     "answer": "Immediately call Ext. 9999. Email details to security@company.com. Do not tamper with evidence."},
    
    {"id": 88, "category": "Security", "keyword": "Access", 
     "question": "Access to restricted areas?", 
     "answer": "Need prior approval from department head and Security. Submit request 48 hours in advance."},
    
    # Facilities (5 FAQs)
    {"id": 96, "category": "Facilities", "keyword": "Maintenance", 
     "question": "AC not working in cabin?", 
     "answer": "Call Facilities at Ext. 1111. Provide location and issue details. Technician dispatched within 2 hours."},
    
    {"id": 97, "category": "Facilities", "keyword": "Cleaning", 
     "question": "Cabin cleaning schedule?", 
     "answer": "Daily cleaning: 7-9 AM, 1-2 PM, 6-7 PM. Deep cleaning on Saturdays. Complaints? Call Ext. 1111."},
    
    {"id": 98, "category": "Facilities", "keyword": "Stationery", 
     "question": "Get office stationery?", 
     "answer": "Available at stationery room (2nd floor). Bulk orders: Submit request in facilities portal."},
    
    {"id": 99, "category": "Facilities", "keyword": "Meeting Room", 
     "question": "Book conference room?", 
     "answer": "Book through Outlook calendar or room booking portal. Max 2 hours per booking. Cancel if not needed."},
    
    {"id": 100, "category": "General", "keyword": "Help", 
     "question": "Need immediate help?", 
     "answer": "For urgent matters:<br>• IT: Ext. 5555<br>• HR: Ext. 4444<br>• Finance: Ext. 3333<br>• Security: Ext. 9999<br>• Admin: Ext. 2222"}
]