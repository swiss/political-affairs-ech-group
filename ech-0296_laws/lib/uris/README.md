# lib/uris

AKN+ELI URI construction/resolution — consolidates the FRBR-URI resolver (`frbr_uri/`, moved here from
`akn-pipeline/packages/frbr_uri`; the two redundant copies, `frbr-uri` and `frbr_uri_tmp`, were dropped).
`pipeline/uri` generates/validates the RFC 6570 construction templates and resolver config that keep this
in sync with `spec/input/schema.yaml`, rather than hand-maintained parallel logic.
