#!/bin/bash

# Ambil nama suite dari argumen pertama
SUITE=$1

# Cek kalau tidak ada argumen
if [ -z "$SUITE" ]; then
    echo "❌ Harap masukkan nama suite. Contoh:"
    echo "./run_tests.sh smoke"
    echo "./run_tests.sh regression"
    exit 1
fi

# Konversi nama suite jadi lowercase (opsional)
SUITE_LOWER=$(echo "$SUITE" | tr '[:upper:]' '[:lower:]')

# Tentukan folder hasil allure
ALLURE_DIR="allure-results"

echo "🔁 Menjalankan test suite: $SUITE_LOWER"
echo "📁 Output allure: $ALLURE_DIR"

# Bersihkan hasil sebelumnya untuk suite ini
rm -rf "$ALLURE_DIR"

# Export env jika kamu gunakan patching di conftest.py
export ALLURE_RESULTS_DIR="$ALLURE_DIR"

# Jalankan pytest berdasarkan marker suite
pytest -m suite_$SUITE_LOWER
if [ $? -ne 0 ]; then
    echo "❌ Test suite $SUITE_LOWER gagal dijalankan."
    exit 1
fi

# Selesai Test
echo "✅ Selesai menjalankan test suite: $SUITE_LOWER"

# Bersihkan hasil sebelumnya untuk suite ini
rm -rf "allure-report/suite_$SUITE_LOWER"

# generate allure report
allure generate allure-results --clean -o "allure-report/suite_$SUITE_LOWER"

# Tampilkan Allure report
echo "✅ Membuka Allure report: suite_$SUITE_LOWER"

# Membuka Allure report
allure open allure-report/suite_$SUITE_LOWER

