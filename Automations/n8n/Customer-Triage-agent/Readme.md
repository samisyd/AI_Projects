AI Customer Support tickets

I built a stateless customer support triage system using v0 (Next.js) and self-hosted n8n, leveraging a structured gpt-4o-mini LLM agent to instantly classify, prioritize, and log incoming tickets to Google Sheets and send email notifications via Gmail.
 
Link to try out: 
https://customer-support-portal-nine.vercel.app 
You will receive an email that your ticket is processed once the workflow is done successfully
 
===========================================================
Prompt for V0 - "Create a modern Customer Support Portal and Admin Dashboard using Tailwind CSS, Shadcn UI components, and Lucide icons.
 
It needs two views or sections:

1. "Submit a Ticket" form: Clean form with fields for Customer Email, Subject, and Description. 

2. "Admin Live Feed": A table showing logged tickets (Status, Email, AI Category, Priority, Summary).
 
Include the Next.js `useClient` React code that intercepts the form submission, converts it to JSON, and sends a POST request to an external n8n webhook URL. Add a visual loading state while waiting for n8n to respond, and dynamically append the processed ticket to the Admin Live Feed when n8n returns the AI-classified data."
 
===========================================================
AI Agent Prompt in N8N workflow - 
You are a data extraction AI and expert at categorizing the customer support tickets based on priority. Analyze the incoming customer ticket subject and description.
 
You must return exactly a JSON object matching this structure:

{

  "category": "Technical",

  "priority": "High" | "Medium" | "Low",

  "summary": "A concise 1-sentence summary of the issue"

}
 
Allowed values for category: "Technical", "Billing", "General"

Allowed values for priority: "High", "Medium", "Low"
 
Ticket Subject: {{ $json.body.subject }}

Ticket Description: {{ $json.body.description }}
===========================================================
 
What triggers it?
The trigger is a User Form Submission on your frontend.
 
When a customer fills out their email, subject, and description on your v0 dashboard and clicks the "Submit" button, it instantly fires an HTTP POST request containing that form data directly to your production n8n webhook URL.
 
What tools does it use?
1. v0 (by Vercel): For the Next.js/React frontend user interface and form dashboard.

2. n8n (Self-hosted on Hostinger VPS): As the backend workflow orchestration engine.

3. OpenAI API (gpt-4o-mini): Configured in native JSON Object mode for structured data extraction.

4. Google Sheets & Gmail: As the production data storage layer and messaging channels.

What does it output?
A new populated row in a Google Sheets triage dashboard and an instant email receipt confirmation via Gmail to the user.
 
Who benefits?
1. Support Agents & Operators: Saves hours of manual work by instantly sorting, labeling, and prioritizing incoming tickets, allowing them to focus directly on solving high-priority issues.

2. End Users / Customers: Receive faster support response times and instant email confirmations, knowing their urgent technical issues are categorized correctly from the start.

3. The Business / Engineering Team: Gains a highly scalable, cost-efficient (pennies per thousand tickets via gpt-4o-mini), and centralized tracking dashboard that keeps analytical metrics structured and error-free.

Why I built it :

To eliminate manual, time-consuming support ticket categorization and minimize initial customer response latency.

Reflection :

Building this helped me understand how we can use multiple AI tools together to build a full-stack application. It showed me how easy it is to design a sleek UI in tools like v0 and connect it smoothly to a backend workflow engine. 

It significantly strengthened my practical understanding of frontend design, backend orchestration in n8n, and structuring LLM outputs natively to match real-world data schemas without throwing errors.

I am really proud of developing a functional, real-world use case. It showed me how daily operational problems can be transformed into smart, highly efficient automation systems that helps save time.
 
Future Improvements:
- Database Persistence (Supabase): Migrate from Google Sheets to Supabase (PostgreSQL) to securely store full ticket records

- Authentication & Authorization: Secure the system by adding user authentication (e.g., via Supabase Auth), ensuring only authorized customer support agents can log into the v0 dashboard to view, update, or resolve tickets.

- Trigger an immediate Slack escalation alerts for tickets flagged with both Technical category and High priority.


Agent design:
 
Modern support ticket system with AI categorization
 