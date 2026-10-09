import unittest

from app import app, SEMESTERS


class SiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_pages_load(self):
        for route in ("/", "/formation", "/vie-etudiante"):
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)

    def test_formation_contains_all_semesters(self):
        response = self.client.get("/formation")
        self.assertEqual(response.status_code, 200)
        for semester in ("S1", "S2", "S3", "S4", "S5", "S6"):
            self.assertIn(semester.encode(), response.data)

    def test_semester_credit_totals(self):
        self.assertEqual([sum(unit[2] for unit in s["units"]) for s in SEMESTERS], [30] * 6)

    def test_unknown_page_returns_custom_404(self):
        response = self.client.get("/inconnue")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Cette page n’existe pas".encode(), response.data)

    def test_contact_alumni_link_present(self):
        response = self.client.get("/vie-etudiante")
        self.assertIn(b"https://www.linkedin.com/in/davidadja/", response.data)
        self.assertIn("Me contacter sur LinkedIn".encode(), response.data)
        self.assertIn("images/david-adja.jpg".encode(), response.data)

    def test_technology_banner_present(self):
        response = self.client.get("/")
        self.assertIn("images/server-network.jpg".encode(), response.data)
        self.assertIn("Réseaux · Systèmes · Cloud".encode(), response.data)


if __name__ == "__main__":
    unittest.main()
