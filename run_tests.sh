#!/bin/bash

# Ambil nama suite dari argumen pertama
SUITE=$1

# Cek kalau tidak ada argumen
if [ -z "$SUITE" ]; then
    echo "❌ Harap masukkan nama suite. Contoh:"
    echo "./run_test_suite.sh smoke"
    echo "./run_test_suite.sh regression"
    exit 1
fi

# Konversi nama suite jadi lowercase (opsional)
SUITE_LOWER=$(echo "$SUITE" | tr '[:upper:]' '[:lower:]')

# Tentukan folder hasil allure
ALLURE_DIR="allure-results/suite_$SUITE_LOWER"
SCREENSHOT_SUBFOLDER="screenshots/suite_$SUITE_LOWER"

echo "🔁 Menjalankan test suite: $SUITE_LOWER"
echo "📁 Output allure: $ALLURE_DIR"

# Bersihkan hasil sebelumnya untuk suite ini
rm -rf "$ALLURE_DIR"

# Bersihkan hasil sebelumnya untuk suite ini
rm -rf "$SCREENSHOT_SUBFOLDER"

# Export env jika kamu gunakan patching di conftest.py
export ALLURE_RESULTS_DIR="$ALLURE_DIR"

# Export supaya bisa dibaca Python
export SCREENSHOT_SUBFOLDER="$SCREENSHOT_SUBFOLDER"


# Jalankan pytest berdasarkan marker suite
pytest -s -v -m suite_$SUITE_LOWER --alluredir="$ALLURE_DIR"
# Jalankan pytest
# pytest -s -v tests/ --alluredir="$ALLURE_DIR"
if [ $? -ne 0 ]; then
    echo "❌ Test suite $SUITE_LOWER gagal dijalankan."
    exit 1
fi

# Selesai Test
echo "✅ Selesai menjalankan test suite: $SUITE_LOWER"

# Hapus folder tests dari allure-results
find allure-results -type d -name "tests" -exec rm -rf {} +

# generate allure report
allure generate "$ALLURE_DIR" --clean -o "allure-report/suite_$SUITE_LOWER"

# Tampilkan Allure report
echo "✅ Membuka Allure report: suite_$SUITE_LOWER"

# Membuka Allure report
allure open allure-report/suite_$SUITE_LOWER

