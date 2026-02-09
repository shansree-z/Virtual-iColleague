from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Simplified FAQ with direct answers + emails when needed
FAQ_SIMPLE = {
    # Emergency - Include email
    "emergency": {
        "answer": "Emergency: Call Ext. 9999 (24/7). Medical: Ext. 8888. Fire: Ext. 7777. Email security: security@company.com",
        "category": "Emergency"
    },
    
    # IT - Include email
    "wifi": {
        "answer": "Connect to 'Corp_Secure'. Username: Employee ID. For issues, email IT: it-support@company.com or call Ext. 5555",
        "category": "IT"
    },
    "password": {
        "answer": "Reset password at password.company.com. Need help? Email: it-helpdesk@company.com or call Ext. 5555",
        "category": "IT"
    },
    "vpn": {
        "answer": "VPN setup: Download from IT portal. Server: vpn.company.com. Issues? Email: vpn-support@company.com",
        "category": "IT"
    },
    
    # HR - Include email
    "salary": {
        "answer": "Salary credited on 28th each month. For delays, email HR: payroll@company.com or call Ext. 4444",
        "category": "HR"
    },
    "leave": {
        "answer": "Apply leave in HR portal. For sick leave >2 days, email: leave-request@company.com with medical certificate",
        "category": "HR"
    },
    "manager": {
        "answer": "Your reporting manager is Sarah Johnson. Contact: sarah.j@company.com, Phone: Ext. 4200",
        "category": "HR"
    },
    
    # Finance - Include email
    "expenses": {
        "answer": "Submit expenses within 15 days via Finance portal. Queries? Email: expenses@company.com or call Ext. 3333",
        "category": "Finance"
    },
    "reimbursement": {
        "answer": "Reimbursement takes 10 working days after approval. Check status or email: reimbursement@company.com",
        "category": "Finance"
    },
    
    # Facilities - Include email
    "meeting room": {
        "answer": "Book rooms via Outlook calendar. For assistance, email: facilities@company.com or call Ext. 1111",
        "category": "Facilities"
    },
    "maintenance": {
        "answer": "AC not working? Email: maintenance@company.com with location details. Call Ext. 1111 for urgent issues",
        "category": "Facilities"
    },
    
    # Admin - Include email
    "id card": {
        "answer": "Lost ID card? Report to Security Desk immediately. Email: admin-security@company.com for replacement",
        "category": "Admin"
    },
    "parking": {
        "answer": "Submit vehicle details to get parking permit. Email: parking-admin@company.com. Call Ext. 2222",
        "category": "Admin"
    },
    
    # General work queries - Include email when relevant
    "work from home": {
        "answer": "Hybrid policy: 3 days office, 2 days WFH. Submit request in HR portal. Email: wfh-approval@company.com for exceptions",
        "category": "Work Policy"
    },
    "overtime": {
        "answer": "Overtime requires manager approval. Paid 1.5x. Submit via HR portal. Email: overtime-hr@company.com for queries",
        "category": "Work Policy"
    }
}

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

@app.route('/')
def home():
    current_time = datetime.now().strftime("%I:%M %p")
    current_date = datetime.now().strftime("%A, %d %B %Y")
    return render_template('index.html', 
                         greeting=get_greeting(),
                         current_time=current_time,
                         current_date=current_date)

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        user_input = data.get('message', '').lower().strip()
        
        # Check greetings
        if any(word in user_input for word in ['hello', 'hi', 'hey']):
            return jsonify({
                'response': f"{get_greeting()}! Ask me about work queries. I'll provide answers with contact emails when needed.",
                'category': 'Welcome'
            })
        
        # Check thanks
        if any(word in user_input for word in ['thank', 'thanks']):
            return jsonify({
                'response': "You're welcome! Need anything else?",
                'category': 'General'
            })
        
        # Search for direct match
        for keyword, info in FAQ_SIMPLE.items():
            if keyword in user_input:
                return jsonify({
                    'response': info['answer'],
                    'category': info['category']
                })
        
        # Partial match search
        user_words = user_input.split()
        for keyword, info in FAQ_SIMPLE.items():
            keyword_words = keyword.split()
            matches = sum(1 for word in user_words if any(kw in word for kw in keyword_words))
            if matches >= len(keyword_words) // 2 + 1:
                return jsonify({
                    'response': info['answer'],
                    'category': info['category']
                })
        
        # Default response with general email
        default_email = "support@company.com"
        return jsonify({
            'response': f"I'm not sure about that specific query. For assistance, please email: {default_email} or call general support at Ext. 1000.",
            'category': 'General'
        })
        
    except Exception as e:
        return jsonify({
            'response': f"System error. Please email: admin-support@company.com for technical issues.",
            'category': 'Error'
        })

@app.route('/get_suggestions')
def get_suggestions():
    suggestions = [
        {"text": "WiFi connection", "query": "How to connect to WiFi?"},
        {"text": "Salary date", "query": "When is salary credited?"},
        {"text": "Expense claim", "query": "How to claim expenses?"},
        {"text": "Meeting room", "query": "How to book meeting room?"},
        {"text": "Work from home", "query": "Can we work from home?"},
        {"text": "Lost ID card", "query": "What if I lost my ID card?"}
    ]
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True, port=5000)