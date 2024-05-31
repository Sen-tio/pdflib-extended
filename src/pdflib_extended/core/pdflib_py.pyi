def PDF_new() -> int:
    pass

def PDF_delete(p: int) -> None:
    pass

def PDF_set_option(p: int, optlist: str) -> None:
    pass

def PDF_activate_item(p: int, id: int) -> None:
    pass

def PDF_add_bookmark(p: int, text: str, parent: int, open: bool) -> int:
    pass

def PDF_add_launchlink(
    p: int, llx: float, lly: float, urx: float, ury: float, filename: str
) -> None:
    pass

def PDF_add_locallink(
    p: int, llx: float, lly: float, urx: float, ury: float, page: int, optlist: str
) -> None:
    pass

def PDF_add_nameddest(p: int, name: str, optlist: str) -> None:
    pass

def PDF_add_note(
    p: int,
    llx: float,
    lly: float,
    urx: float,
    ury: float,
    contents: str,
    title: str,
    icon: str,
    open: bool,
) -> None:
    pass

def PDF_add_path_point(
    p: int, path: str, x: float, y: float, type: str, optlist: str
) -> int:
    pass

def PDF_add_pdflink(
    p: int,
    llx: float,
    lly: float,
    urx: float,
    ury: float,
    filename: str,
    page: int,
    optlist: str,
) -> None:
    pass

def PDF_add_portfolio_file(p: int, folder: int, filename: str, optlist: str) -> int:
    pass

def PDF_add_portfolio_folder(p: int, parent: int, foldername: str, optlist: str) -> int:
    pass

def PDF_add_table_cell(
    p: int, table: int, column: int, row: int, text: str, optlist: str
) -> int:
    pass

def PDF_add_textflow(p: int, textflow: int, text: str, optlist: str) -> int:
    pass

def PDF_add_thumbnail(p: int, image: int) -> None:
    pass

def PDF_add_weblink(
    p: int, llx: float, lly: float, urx: float, ury: float, url: str
) -> None:
    pass

def PDF_align(p: int, dx: float, dy: float) -> None:
    pass

def PDF_arc(p: int, x: float, y: float, r: float, alpha: float, beta: float) -> None:
    pass

def PDF_arcn(p: int, x: float, y: float, r: float, alpha: float, beta: float) -> None:
    pass

def PDF_attach_file(
    p: int,
    llx: float,
    lly: float,
    urx: float,
    ury: float,
    filename: str,
    description: float,
    author: float,
    mimetype: str,
    icon: int,
) -> None:
    pass

def PDF_begin_document(p: int, filename: str, optlist: str) -> int:
    pass

def PDF_begin_dpart(p: int, optlist: str) -> None:
    pass

def PDF_begin_font(
    p: int,
    fontname: str,
    a: float,
    b: float,
    c: float,
    d: float,
    e: float,
    f: float,
    optlist: str,
) -> None:
    pass

def PDF_begin_glyph(
    p: int, glyphname: str, wx: int, llx: float, lly: float, urx: float, ury: float
) -> None:
    pass

def PDF_begin_glyph_ext(p: int, uv: int, optlist: str) -> None:
    pass

def PDF_begin_item(p: int, tagname: str, optlist: str) -> int:
    pass

def PDF_begin_layer(p: int, layer: int) -> None:
    pass

def PDF_begin_mc(p: int, tagname: str, optlist: str) -> None:
    pass

def PDF_begin_page(p: int, width: float, height: float) -> None:
    pass

def PDF_begin_page_ext(p: int, width: float, height: float, optlist: str) -> None:
    pass

def PDF_begin_pattern(
    p: int, width: float, height: float, xstep: float, ystep: float, painttype: int
) -> int:
    pass

def PDF_begin_pattern_ext(p: int, width: float, height: float, optlist: str) -> int:
    pass

def PDF_begin_template(p: int, width: float, height: float) -> int:
    pass

def PDF_begin_template_ext(p: int, width: float, height: float, optlist: str) -> int:
    pass

def PDF_circle(p: int, x: float, y: float, r: float) -> None:
    pass

def PDF_circular_arc(p: int, x1: float, y1: float, x2: float, y2: float) -> None:
    pass

def PDF_clip(p: int) -> None:
    pass

def PDF_close(p: int) -> None:
    pass

def PDF_close_font(p: int, font: int) -> None:
    pass

def PDF_close_graphics(p: int, graphics: int) -> None:
    pass

def PDF_close_image(p: int, image: int) -> None:
    pass

def PDF_close_pdi(p: int, doc: int) -> None:
    pass

def PDF_close_pdi_document(p: int, doc: int) -> None:
    pass

def PDF_close_pdi_page(p: int, page: int) -> None:
    pass

def PDF_closepath(p: int) -> None:
    pass

def PDF_closepath_fill_stroke(p: int) -> None:
    pass

def PDF_closepath_stroke(p: int) -> None:
    pass

def PDF_concat(
    p: int, a: float, b: float, c: float, d: float, e: float, f: float
) -> None:
    pass

def PDF_continue_text(p: int, text: str) -> None:
    pass

def PDF_convert_to_unicode(
    p: int, inputformat: str, inputstring: str, optlist: str
) -> str:
    pass

def PDF_create_3dview(p: int, username: str, optlist: str) -> int:
    pass

def PDF_create_action(p: int, type: str, optlist: str) -> int:
    pass

def PDF_create_annotation(
    p: int, llx: float, lly: float, urx: float, ury: float, type: str, optlist: str
) -> None:
    pass

def PDF_create_devicen(p: int, optlist: str) -> int:
    pass

def PDF_create_bookmark(p: int, text: str, optlist: str) -> int:
    pass

def PDF_create_field(
    p: int,
    llx: float,
    lly: float,
    urx: float,
    ury: float,
    name: str,
    type: str,
    optlist: str,
) -> None:
    pass

def PDF_create_fieldgroup(p: int, name: str, optlist: str) -> None:
    pass

def PDF_create_gstate(p: int, optlist: str) -> int:
    pass

def PDF_create_pvf(p: int, filename: str, data: str, optlist: str):
    pass
