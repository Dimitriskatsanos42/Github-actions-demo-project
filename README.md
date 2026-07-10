# GitHub Actions Demo Project

![CI](https://github.com/Dimitriskatsanos42/Github-actions-demo-project/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Ένα μικρό αλλά ολοκληρωμένο demo project που δείχνει πώς στήνεται ένα
**CI/CD pipeline** με **GitHub Actions** πάνω σε ένα απλό Python module.

Το project υπάρχει καθαρά για εκπαιδευτικούς/showcase λόγους: δείχνει
testing, linting, matrix builds σε πολλαπλές εκδόσεις Python, και
αυτοματοποιημένα releases.

## 📂 Δομή project

```
.
├── .github/workflows/
│   ├── ci.yml          # Τρέχει tests + lint σε κάθε push/PR
│   └── release.yml      # Δημιουργεί GitHub Release σε κάθε version tag
├── calculator.py         # Ο πυρήνας της εφαρμογής
├── test_calculator.py    # Unit tests (pytest)
├── requirements.txt       # Dependencies
├── .flake8                # Ρυθμίσεις linter
└── README.md
```

## ⚙️ Τι κάνει το CI pipeline

Σε κάθε `push` ή `pull request` προς το `main`:

1. Κάνει checkout τον κώδικα
2. Στήνει Python (matrix: 3.10, 3.11, 3.12)
3. Εγκαθιστά τα dependencies
4. Τρέχει `flake8` για linting
5. Τρέχει `pytest` για τα unit tests

Αν οποιοδήποτε βήμα αποτύχει, το build κοκκινίζει και φαίνεται άμεσα
στο badge πάνω στο README και στο tab **Actions** του repository.

## 🚀 Πώς δημιουργείται ένα Release (CD)

```bash
git tag v1.0.0
git push origin v1.0.0
```

Αυτό ενεργοποιεί το `release.yml`, το οποίο ξανατρέχει τα tests και,
αν περάσουν, δημιουργεί αυτόματα ένα GitHub Release με auto-generated
release notes.

## 🖥️ Τοπική εκτέλεση

```bash
# Εγκατάσταση dependencies
pip install -r requirements.txt

# Εκτέλεση του calculator
python calculator.py

# Εκτέλεση των tests
pytest -v

# Linting
flake8 .
```

## 📈 Πιθανές επεκτάσεις

- Προσθήκη `black`/`isort` για αυτόματο formatting
- Publish σε PyPI μέσω `release.yml`
- Docker image build & push σε GHCR
- Code coverage report (π.χ. `pytest-cov` + Codecov badge)

## 📄 Άδεια χρήσης

Το project διανέμεται υπό την άδεια MIT — δες το αρχείο [LICENSE](LICENSE).
