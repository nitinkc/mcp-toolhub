# Deployment

## GitHub Pages (Recommended)

The easiest way to share your docs publicly — free hosting via GitHub Pages.

### Automatic deployment with GitHub Actions

A GitHub Actions workflow is included at `.github/workflows/docs.yml`.  
Every push to `main` automatically builds and deploys the docs.

**Setup:**

1. Push the repo to GitHub
2. Go to **Settings → Pages → Source** → set to `gh-pages` branch
3. Your docs will be live at `https://YOUR_USERNAME.github.io/mcp-toolhub`

---

### Manual deployment

```shell
# Install mkdocs-material if not already installed
pip install mkdocs-material

# Preview locally
mkdocs serve

# Deploy to GitHub Pages
mkdocs gh-deploy --force
```

---

## Local Preview

```shell
cd mcp-toolhub
mkdocs serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
Changes to any `.md` file are hot-reloaded automatically.

---

## Update `mkdocs.yml`

Before deploying, update these fields in `mkdocs.yml`:

```yaml
site_url: https://YOUR_USERNAME.github.io/mcp-toolhub
repo_url: https://github.com/YOUR_USERNAME/mcp-toolhub
repo_name: YOUR_USERNAME/mcp-toolhub
```

Replace `YOUR_USERNAME` with your actual GitHub username.

