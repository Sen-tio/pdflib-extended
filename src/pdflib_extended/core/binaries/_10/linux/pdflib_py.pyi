from typing import Any, Union

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

def PDF_create_pvf(p: int, filename: str, data: str, optlist: str) -> None:
    pass

def PDF_create_textflow(p: int, text: str, optlist: str) -> int:
    pass

def PDF_curveto(
    p: int, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> None:
    pass

def PDF_define_layer(p: int, text: str, optlist: str) -> int:
    pass

def PDF_delete_path(p: int, path: int) -> None:
    pass

def PDF_delete_pvf(p: int, filename: str) -> int:
    pass

def PDF_delete_table(p: int, table: int, optlist: int) -> None:
    pass

def PDF_delete_textflow(p: int, textflow: int) -> None:
    pass

def PDF_draw_path(p: int, path: int, x: float, y: float, optlist: str) -> None:
    pass

def PDF_ellipse(p: int, x: float, y: float, rx: float, ry: float) -> None:
    pass

def PDF_elliptical_arc(
    p: int, x: float, y: float, rx: float, ry: float, optlist: str
) -> None:
    pass

def PDF_encoding_set_char(
    p: int, encoding: str, slot: int, glyphname: str, uv: int
) -> None:
    pass

def PDF_end_document(p: int, optlist: str) -> None:
    pass

def PDF_end_dpart(p: int, optlist: str) -> None:
    pass

def PDF_end_font(p: int) -> None:
    pass

def PDF_end_glyph(p: int) -> None:
    pass

def PDF_end_item(p: int, id: int) -> None:
    pass

def PDF_end_layer(p: int) -> None:
    pass

def PDF_end_mc(p: int) -> None:
    pass

def PDF_end_page(p: int) -> None:
    pass

def PDF_end_page_ext(p: int, optlist: str) -> None:
    pass

def PDF_end_pattern(p: int) -> None:
    pass

def PDF_end_template(p: int) -> None:
    pass

def PDF_end_template_ext(p: int, width: float, height: float) -> None:
    pass

def PDF_endpath(p: int) -> None:
    pass

def PDF_fill(p: int) -> None:
    pass

def PDF_fill_graphicsblock(
    p: int, page: int, blockname: int, graphics: int, optlist: str
) -> int:
    pass

def PDF_fill_imageblock(
    p: int, page: int, blockname: str, image: int, optlist: str
) -> int:
    pass

def PDF_fill_pdfblock(
    p: int, page: int, blockname: str, contents: int, optlist: str
) -> int:
    pass

def PDF_fill_stroke(p: int) -> None:
    pass

def PDF_fill_textblock(
    p: int, block: int, blockname: str, text: str, optlist: str
) -> int:
    pass

def PDF_findfont(p: int, fontname: str, encoding: str, embed: bool) -> int:
    pass

def PDF_fit_graphics(p: int, graphics: int, x: float, y: float, optlist: str) -> None:
    pass

def PDF_fit_image(p: int, image: int, x: float, y: float, optlist: str) -> None:
    pass

def PDF_fit_pdi_page(p: int, page: int, x: float, y: float, optlist: str) -> None:
    pass

def PDF_fit_table(
    p: int, table: int, llx: float, lly: float, urx: float, ury: float, optlist: str
) -> str:
    pass

def PDF_fit_textflow(
    p: int, textflow: int, llx: float, lly: float, urx: float, ury: float, optlist: str
) -> str:
    pass

def PDF_fit_textline(p: int, text: str, x: float, y: float, optlist: str) -> None:
    pass

def PDF_get_apiname(p: int) -> str:
    pass

def PDF_get_buffer(p: int) -> str:
    pass

def PDF_get_errmsg(p: int) -> str:
    pass

def PDF_get_errnum(p: int) -> int:
    pass

def PDF_get_option(p: int, keyword: str, optlist: str) -> float:
    pass

def PDF_get_parameter(p: int, key: str, modifer: float) -> str:
    pass

def PDF_get_pdi_parameter(p: int, key: str, doc: int, page: int, reserved: bool) -> str:
    pass

def PDF_get_pdi_value(p: int, key: str, doc: int, page: int, reserved: int) -> str:
    pass

def PDF_get_string(p: int, idx: int, optlist: str) -> str:
    pass

def PDF_get_value(p: int, key: str, modifier: float) -> float:
    pass

def PDF_info_font(p: int, font: int, keyword: str, optlist: str) -> float:
    pass

def PDF_info_graphics(p: int, graphics: int, keyword: str, optlist: str) -> float:
    pass

def PDF_info_image(p: int, image: int, keyword: str, optlist: str) -> float:
    pass

def PDF_info_matchbox(p: int, boxname: str, num: int, keyword: str) -> float:
    pass

def PDF_info_path(p: int, path: int, keyword: str, optlist: str) -> float:
    pass

def PDF_info_pdi_page(p: int, page: int, keyword: str, optlist: str) -> float:
    pass

def PDF_info_pvf(p: int, filename: str, keyword: str) -> float:
    pass

def PDF_info_table(p: int, table: int, keyword: str) -> float:
    pass

def PDF_info_textflow(p: int, textflow: int, keyword: str) -> float:
    pass

def PDF_info_textline(p: int, text: str, keyword: str, optlist: str) -> float:
    pass

def PDF_initgraphics(p: int) -> None:
    pass

def PDF_lineto(p: int, x: float, y: float) -> None:
    pass

def PDF_load_3ddata(p: int, filename: str, optlist: str) -> int:
    pass

def PDF_load_asset(p: int, type: str, filename: str, optlist: str) -> None:
    pass

def PDF_load_font(p: int, fontname: str, encoding: str, optlist: str) -> int:
    pass

def PDF_load_graphics(p: int, type: str, filename: str, optlist: str) -> int:
    pass

def PDF_load_iccprofile(p: int, profilename: str, optlist: str) -> int:
    pass

def PDF_load_image(p: int, imagetype: str, filename: str, optlist: str) -> int:
    pass

def PDF_makespotcolor(p: int, spotname: str) -> int:
    pass

def PDF_mc_point(p: int, tagname: str, optlist: str) -> None:
    pass

def PDF_moveto(p: int, x: float, y: float) -> None:
    pass

def PDF_open_CCITT(
    p: int,
    filename: str,
    width: float,
    height: float,
    BitReverse: bool,
    k: int,
    BlackIs1: bool,
) -> int:
    pass

def PDF_open_file(p: int, filename: str) -> int:
    pass

def PDF_open_image(
    p: int,
    imagetype: str,
    source: Any,
    data: Any,
    width: float,
    height: float,
    components: Any,
    bpc: Any,
    parameters: Any,
) -> int:
    pass

def PDF_open_image_file(
    p: int, imagetype: str, filename: str, stringparam: str, intparam: int
) -> int:
    pass

def PDF_open_pdi(p: int, filename: str, filename_len: int) -> int:
    pass

def PDF_open_pdi_document(p: int, filename: str, optlist: str) -> int:
    pass

def PDF_open_pdi_page(p: int, doc: int, pagenumber: int, optlist: str) -> int:
    pass

def PDF_pcos_get_number(p: int, doc: int, path: str) -> float:
    pass

def PDF_pcos_get_string(p: int, doc: int, path: str) -> str:
    pass

def PDF_pcos_get_stream(p: int, doc: int, optlist: str, path: str) -> Any:
    pass

def PDF_place_image(p: int, image: int, x: float, y: float, scale: float) -> None:
    pass

def PDF_place_pdi_page(
    p: int, page: int, x: float, y: float, sx: float, sy: float
) -> None:
    pass

def PDF_poca_delete(p: int, container: int, optlist: str) -> None:
    pass

def PDF_poca_insert(p: int, container: int, optlist: str) -> None:
    pass

def PDF_poca_new(p: int, optlist: str) -> int:
    pass

def PDF_poca_remove(p: int, container: int, optlist: str) -> None:
    pass

def PDF_process_pdi(p: int, doc: int, page: int, optlist: str) -> int:
    pass

def PDF_rect(p: int, x: float, y: float, width: float, height: float) -> None:
    pass

def PDF_restore(p: int) -> None:
    pass

def PDF_resume_page(p: int, optlist: str) -> None:
    pass

def PDF_rotate(p: int, phi: float) -> None:
    pass

def PDF_save(p: int) -> None:
    pass

def PDF_scale(p: int, sx: float, sy: float) -> None:
    pass

def PDF_set_border_color(p: int, red: float, green: float, blue: float) -> None:
    pass

def PDF_set_border_dash(p: int, b: float, w: float) -> None:
    pass

def PDF_set_border_style(p: int, style: str, width: float) -> None:
    pass

def PDF_set_graphics_option(p: int, optlist: str) -> None:
    pass

def PDF_set_gstate(p: int, gstate: int) -> None:
    pass

def PDF_set_info(p: int, key: str, value: str) -> None:
    pass

def PDF_set_layer_dependency(p: int, type: str, optlist: str) -> None:
    pass

def PDF_set_parameter(p: int, key: str, value: str) -> None:
    pass

def PDF_set_text_option(p: int, optlist: str) -> None:
    pass

def PDF_set_text_pos(p: int, x: float, y: float) -> None:
    pass

def PDF_set_value(p: int, key: str, value: float) -> None:
    pass

def PDF_setcolor(
    p: int, fstype: str, colorspace: str, c1: float, c2: float, c3: float, c4: float
) -> None:
    pass

def PDF_setdash(p: int, b: float, w: float) -> None:
    pass

def PDF_setdashpattern(p: int, optlist: str) -> None:
    pass

def PDF_setflat(p: int, flatness: float) -> None:
    pass

def PDF_setfont(p: int, font: int, fontsize: float) -> None:
    pass

def PDF_setgray(p: int, gray: float) -> None:
    pass

def PDF_setgray_fill(p: int, gray: float) -> None:
    pass

def PDF_setgray_stroke(p: int, gray: float) -> None:
    pass

def PDF_setlinecap(p: int, linecap: Union[str, int]) -> None:
    pass

def PDF_setlinejoin(p: int, linejoin: Union[str, int]) -> None:
    pass

def PDF_setlinewidth(p: int, width: float) -> None:
    pass

def PDF_setmatrix(
    p: int, a: float, b: float, c: float, d: float, e: float, f: float
) -> None:
    pass

def PDF_setmiterlimit(p: int, miter: float) -> None:
    pass

def PDF_setpolydash(p: int, dasharray: list[Union[str, float]], length: int) -> None:
    pass

def PDF_setrgbcolor(p: int, red: float, green: float, blue: float) -> None:
    pass

def PDF_setrgbcolor_fill(p: int, red: float, green: float, blue: float) -> None:
    pass

def PDF_setrgbcolor_stroke(p: int, red: float, green: float, blue: float) -> None:
    pass

def PDF_shading(
    p: int,
    type: str,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
    c1: float,
    c2: float,
    c3: float,
    c4: float,
    optlist: str,
) -> int:
    pass

def PDF_shading_pattern(p: int, shading: int, optlist: str) -> int:
    pass

def PDF_shfill(p: int, shading: int) -> None:
    pass

def PDF_show(p: int, text: str) -> None:
    pass

def PDF_show_boxed(
    p: int,
    text: str,
    left: float,
    top: float,
    width: float,
    height: float,
    hmode: Any,
    feature: Any,
) -> int:
    pass

def PDF_show_xy(p: int, text: str, x: float, y: float) -> None:
    pass

def PDF_skew(p: int, alpha: float, beta: float) -> None:
    pass

def PDF_stringwidth(p: int, text: str, font: int, fontsize: float) -> float:
    pass

def PDF_stroke(p: int) -> None:
    pass

def PDF_suspend_page(p: int, optlist: str) -> None:
    pass

def PDF_translate(p: int, tx: float, ty: float) -> None:
    pass