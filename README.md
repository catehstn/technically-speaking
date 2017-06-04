# Technically Speaking

The Open Source repository for the [Technically Speaking newsletter](http://www.techspeak.email/).

## We want links from you!

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Internal notes: Adding tweet it links

Run it like this
`./scripts/tweet-it.py 2016/05-May/10.md`

The markdown needs to have something like `[[read it](link)][tweet it]`

The placeholder `[tweet it]` is then replaced with `[[tweet it](url)]` with the appropriate tweet it url. Double check to make sure the resulting tweet isn't too long. If so, you will need to edit it manually.
