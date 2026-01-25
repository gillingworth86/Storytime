const KIT_API_URL = 'https://api.kit.com/v4/forms';

function isValidEmail(email) {
  if (typeof email !== 'string') {
    return false;
  }
  const trimmed = email.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(trimmed) && trimmed.length <= 254 && trimmed.length >= 5;
}

function normalizeFormId(formId) {
  if (typeof formId !== 'string') {
    return null;
  }
  const trimmed = formId.trim();
  if (!trimmed) {
    return null;
  }
  if (/^\d+$/.test(trimmed)) {
    return trimmed;
  }
  const match = trimmed.match(/forms\/(\d+)/i) || trimmed.match(/(\d{4,})/);
  return match ? match[1] : null;
}

async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed.' });
  }

  const apiKey = process.env.KIT_API_KEY;
  const formId = normalizeFormId(process.env.KIT_FORM_ID);

  if (!apiKey || !formId) {
    return res.status(500).json({ error: 'Missing or invalid Kit configuration.' });
  }

  const { email, location, signup_url: signupUrl, referrer, tags } = req.body || {};

  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email address.' });
  }

  const metadata = {
    signup_location: location || 'unknown',
    signup_date: new Date().toISOString(),
    signup_url: signupUrl || '',
    referrer: referrer || ''
  };

  const requestBody = {
    email: email.trim().toLowerCase(),
    tags: Array.isArray(tags) ? tags : undefined,
    fields: metadata
  };

  try {
    // On older Node runtimes (<18) global fetch may not exist.
    // If you see "fetch is not defined" in logs, install node-fetch and uncomment:
    // const fetch = global.fetch || (await import('node-fetch')).default;
    const response = await fetch(`${KIT_API_URL}/${formId}/subscribers`, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      return res.status(response.status).json({
        error: data.message || 'Kit request failed.',
        details: data
      });
    }

    return res.status(200).json({ success: true });
  } catch (error) {
    // Surface error into logs so you can see details in Vercel logs
    console.error('subscribe error:', error);
    return res.status(500).json({ error: 'Failed to reach Kit.' });
  }
}

module.exports = handler;