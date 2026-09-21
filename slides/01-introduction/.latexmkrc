# Make the shared theme in slides/theme/ visible and keep build files out of the way.
ensure_path('TEXINPUTS', '../theme//');
$pdf_mode = 1;
$out_dir  = 'build';
@default_files = ('main.tex');
