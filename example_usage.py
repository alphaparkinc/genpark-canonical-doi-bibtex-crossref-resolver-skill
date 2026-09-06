from client import CanonicalDoiBibtexCrossrefResolverClient

def main():
    client = CanonicalDoiBibtexCrossrefResolverClient()
    res = client.resolve_canonical_bibtex()
    print('DOI BibTeX Resolver: ' + res['resolution_id'] + ' (Verified: ' + str(res['crossref_verified']) + ')')
    print('Title: ' + res['canonical_title'])
    print('Export URL: ' + res['bibtex_export_url'])

if __name__ == '__main__':
    main()
