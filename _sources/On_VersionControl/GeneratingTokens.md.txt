# Generating a Personal Access Token in GitHub

Using a **Personal Access Token** or PAT is the standard way to authenticate when using the command line or the API. GitHub now offers two types: **Fine-grained** (recommended) and **Classic**.

## 1. Navigate to Developer Settings\

1. Log in to your GitHub account.
2. Click your **profile photo** in the top-right corner and select **Settings**.
3. In the left-hand sidebar, scroll all the way to the bottom and click **Developer settings**.

## 2. Choose Your Token Type

On the left sidebar, click **Personal access tokens**. You will see two options:

### Option A: Fine-grained tokens (Recommended)

*Best for specific projects. You can limit access to specific repositories.*

1. Click **Fine-grained tokens** -> **Generate new token**.
2. **Name & Expiration:** Give it a name and set an expiry (default is 30 days).
3. **Resource owner:** Select your account (or an organization).
4. **Repository access:** Choose **"Only select repositories"** to keep things secure.
5. **Permissions:** Under **Repository permissions**, find what you need. (For basic git actions like push/pull, set **Contents** to "Read and write").
6. Click **Generate token**.

### Option B: Tokens (classic)

*Best for general use or older tools that don't support fine-grained permissions.*

1. Click **Tokens (classic)** -> **Generate new token (classic)**.
2. **Note:** Enter a description (e.g., "Home PC Access").
3. **Expiration:** Select a duration.
4. **Scopes:** For general command-line use, check the **`repo`** box (this grants full control of private and public repositories).
5. Click **Generate token**.

---

## 3. Save Your Token

> [!IMPORTANT]
> **Copy the token immediately.** GitHub will never show it to you again. If you lose it, you’ll have to delete it and create a new one.

### How to use it

When your terminal (or VS Code) asks for your GitHub password, **paste the token instead of your actual password**.

**Pro-tip:** If you find yourself pasting this constantly, you can save it globally using:
`git config --global credential.helper store`
