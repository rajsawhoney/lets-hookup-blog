import { Pipeline, Log } from '@ephox/agar';
import { UnitTest } from '@ephox/bedrock-client';
import { LegacyUnit, TinyLoader } from '@ephox/mcagar';

import Editor from 'tinymce/core/api/Editor';
import Env from 'tinymce/core/api/Env';
import Plugin from 'tinymce/plugins/lists/Plugin';
import Theme from 'tinymce/themes/silver/Theme';

UnitTest.asynctest('tinymce.lists.browser.ApplyTest', (success, failure) => {
  const suite = LegacyUnit.createSuite<Editor>();

  Plugin();
  Theme();

  suite.test('TestCase-TBA: Lists: Apply UL list to single P', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(), '<ul><li>a</li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to single empty P', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p><br></p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(LegacyUnit.trimBrs(editor.getContent({ format: 'raw' })), '<ul><li></li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to multiple Ps', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>' +
      '<p>b</p>' +
      '<p>c</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0, 'p:last', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL list to single P', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getContent(), '<ol><li>a</li></ol>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL list to single empty P', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p><br></p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(LegacyUnit.trimBrs(editor.getContent({ format: 'raw' })), '<ol><li></li></ol>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL list to multiple Ps', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>' +
      '<p>b</p>' +
      '<p>c</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0, 'p:last', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ol>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL to UL list', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'li', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ol>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test(
    'Apply OL to UL list with collapsed selection',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ul>' +
        '<li>a</li>' +
        '<li>b</li>' +
        '<li>c</li>' +
        '</ul>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'li:nth-child(2)', 0);
      LegacyUnit.execCommand(editor, 'InsertOrderedList');

      LegacyUnit.equal(editor.getContent(),
        '<ol>' +
        '<li>a</li>' +
        '<li>b</li>' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test('TestCase-TBA: Lists: Apply UL to OL list', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ol>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'li', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL to OL list collapsed selection', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ol>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'li:nth-child(2)', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL to P and merge with adjacent lists', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ul>' +
      '<li>a</li>' +
      '</ul>' +
      '<p>b</p>' +
      '<ul>' +
      '<li>c</li>' +
      '</ul>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 1);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL to OL and merge with adjacent lists', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ul>' +
      '<li>a</li>' +
      '</ul>' +
      '<ol><li>b</li></ol>' +
      '<ul>' +
      '<li>c</li>' +
      '</ul>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'ol li', 1);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL to P and merge with adjacent lists', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ol>' +
      '<li>a</li>' +
      '</ol>' +
      '<p>b</p>' +
      '<ol>' +
      '<li>c</li>' +
      '</ol>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 1);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ol>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply OL to UL and merge with adjacent lists', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<ol>' +
      '<li>1a</li>' +
      '<li>1b</li>' +
      '</ol>' +
      '<ul><li>2a</li><li>2b</li></ul>' +
      '<ol>' +
      '<li>3a</li>' +
      '<li>3b</li>' +
      '</ol>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'ul li', 1);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ol>' +
      '<li>1a</li>' +
      '<li>1b</li>' +
      '<li>2a</li>' +
      '<li>2b</li>' +
      '<li>3a</li>' +
      '<li>3b</li>' +
      '</ol>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
  });

  suite.test(
    'Apply OL to UL and DO not merge with adjacent lists because styles are different (exec has style)',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol>' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol>' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList', null, { 'list-style-type': 'lower-alpha' });

      LegacyUnit.equal(editor.getContent(),
        '<ol>' +
        '<li>a</li>' +
        '</ol>' +
        '<ol style="list-style-type: lower-alpha;"><li>b</li></ol>' +
        '<ol>' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to P and DO not merge with adjacent lists because styles are different (exec has style)',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol>' +
        '<li>a</li>' +
        '</ol>' +
        '<p>b</p>' +
        '<ol>' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'p', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList', null, { 'list-style-type': 'lower-alpha' });

      LegacyUnit.equal(editor.getContent(),
        '<ol>' +
        '<li>a</li>' +
        '</ol>' +
        '<ol style="list-style-type: lower-alpha;"><li>b</li></ol>' +
        '<ol>' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to UL and DO not merge with adjacent lists because styles are different (original has style)',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol style="list-style-type: upper-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList');

      LegacyUnit.equal(editor.getContent(),
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ol><li>b</li></ol>' +
        '<ol style="list-style-type: upper-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to UL should merge with adjacent lists because styles are the same (both have roman)',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol style="list-style-type: upper-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList', false, { 'list-style-type': 'upper-roman' });

      LegacyUnit.equal(editor.getContent(),
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '<li>b</li>' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to UL should merge with above list because styles are the same (both have lower-roman), but not below list',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol style="list-style-type: lower-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol style="list-style-type: upper-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList', false, { 'list-style-type': 'lower-roman' });

      LegacyUnit.equal(editor.getContent(),
        '<ol style="list-style-type: lower-roman;">' +
        '<li>a</li>' +
        '<li>b</li>' +
        '</ol>' +
        '<ol style="list-style-type: upper-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to UL should merge with below lists because styles are the same (both have roman), but not above list',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol style="list-style-type: lower-roman;">' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList', false, { 'list-style-type': 'lower-roman' });

      LegacyUnit.equal(editor.getContent(),
        '<ol style="list-style-type: upper-roman;">' +
        '<li>a</li>' +
        '</ol>' +
        '<ol style="list-style-type: lower-roman;">' +
        '<li>b</li>' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test(
    'Apply OL to UL and DO not merge with adjacent lists because classes are different',
    function (editor) {
      editor.getBody().innerHTML = LegacyUnit.trimBrs(
        '<ol class="a">' +
        '<li>a</li>' +
        '</ol>' +
        '<ul><li>b</li></ul>' +
        '<ol class="b">' +
        '<li>c</li>' +
        '</ol>'
      );

      editor.focus();
      LegacyUnit.setSelection(editor, 'ul li', 1);
      LegacyUnit.execCommand(editor, 'InsertOrderedList');

      LegacyUnit.equal(editor.getContent(),
        '<ol class="a">' +
        '<li>a</li>' +
        '</ol>' +
        '<ol><li>b</li></ol>' +
        '<ol class="b">' +
        '<li>c</li>' +
        '</ol>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test('TestCase-TBA: Lists: Apply UL list to single text line', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      'a'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'body', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(), '<ul><li>a</li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');

    editor.settings.forced_root_block = 'p';
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to single text line with BR', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      'a<br>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'body', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(), '<ul><li>a</li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');

    editor.settings.forced_root_block = 'p';
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to multiple lines separated by BR', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      'a<br>' +
      'b<br>' +
      'c'
    );

    editor.focus();
    editor.execCommand('SelectAll');
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');

    editor.settings.forced_root_block = 'p';
  });

  suite.test(
    'Apply UL list to multiple lines separated by BR and with trailing BR',
    function (editor) {
      editor.settings.forced_root_block = false;

      editor.getBody().innerHTML = (
        'a<br>' +
        'b<br>' +
        'c<br>'
      );

      editor.focus();
      editor.execCommand('SelectAll');
      LegacyUnit.execCommand(editor, 'InsertUnorderedList');

      LegacyUnit.equal(editor.getContent(),
        '<ul>' +
        '<li>a</li>' +
        '<li>b</li>' +
        '<li>c</li>' +
        '</ul>'
      );
      LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    }
  );

  suite.test('TestCase-TBA: Lists: Apply UL list to multiple formatted lines separated by BR', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      '<strong>a</strong><br>' +
      '<span>b</span><br>' +
      '<em>c</em>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'strong', 0, 'em', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li><strong>a</strong></li>' +
      '<li><span>b</span></li>' +
      '<li><em>c</em></li>' +
      '</ul>'
    );

    LegacyUnit.equal(editor.selection.getStart().nodeName, 'STRONG');
    // Old IE will return the end LI not a big deal
    LegacyUnit.equal(editor.selection.getEnd().nodeName, Env.ie && Env.ie < 9 ? 'LI' : 'EM');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to br line and text block line', function (editor) {
    editor.settings.forced_root_block = false;

    editor.setContent(
      'a' +
      '<p>b</p>'
    );

    const rng = editor.dom.createRng();
    rng.setStart(editor.getBody().firstChild, 0);
    rng.setEnd(editor.getBody().lastChild.firstChild, 1);
    editor.selection.setRng(rng);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '</ul>'
    );

    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    LegacyUnit.equal(editor.selection.getEnd().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to text block line and br line', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      '<p>a</p>' +
      'b'
    );

    editor.focus();
    const rng = editor.dom.createRng();
    rng.setStart(editor.getBody().firstChild.firstChild, 0);
    rng.setEnd(editor.getBody().lastChild, 1);
    editor.selection.setRng(rng);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '</ul>'
    );

    LegacyUnit.equal(editor.selection.getStart().nodeName, 'LI');
    LegacyUnit.equal(editor.selection.getEnd().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to all BR lines (SelectAll)', function (editor) {
    editor.settings.forced_root_block = false;

    editor.getBody().innerHTML = (
      'a<br>' +
      'b<br>' +
      'c<br>'
    );

    editor.focus();
    editor.execCommand('SelectAll');
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );

    editor.settings.forced_root_block = 'p';
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to all P lines (SelectAll)', function (editor) {
    editor.getBody().innerHTML = (
      '<p>a</p>' +
      '<p>b</p>' +
      '<p>c</p>'
    );

    editor.focus();
    editor.execCommand('SelectAll');
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(),
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li>c</li>' +
      '</ul>'
    );
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to single P', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(), '<ul><li>a</li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to more than two paragraphs', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p>a</p>' +
      '<p>b</p>' +
      '<p>c</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p:nth-child(1)', 0, 'p:nth-child(3)', 1);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList', false, { 'list-style-type': null });

    LegacyUnit.equal(editor.getContent(), '<ul><li>a</li><li>b</li><li>c</li></ul>');
  });

  suite.test('TestCase-TBA: Lists: Apply UL with custom attributes', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs('<p>a</p>');

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList', false, {
      'list-attributes': {
        'class': 'a',
        'data-custom': 'c1'
      }
    });

    LegacyUnit.equal(editor.getContent(), '<ul class="a" data-custom="c1"><li>a</li></ul>');
  });

  suite.test('TestCase-TBA: Lists: Apply UL and LI with custom attributes', function (editor) {
    editor.getBody().innerHTML = LegacyUnit.trimBrs('<p>a</p>');

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList', false, {
      'list-attributes': {
        'class': 'a',
        'data-custom': 'c1'
      },

      'list-item-attributes': {
        'class': 'b',
        'data-custom1': 'c2',
        'data-custom2': ''
      }
    });

    LegacyUnit.equal(editor.getContent(), '<ul class="a" data-custom="c1"><li class="b" data-custom1="c2" data-custom2="">a</li></ul>');
  });

  suite.test('TestCase-TBA: Lists: Handle one empty unordered list items without error', function (editor) {
    editor.getBody().innerHTML = (
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li></li>' +
      '</ul>'
    );

    editor.execCommand('SelectAll');
    LegacyUnit.setSelection(editor, 'li:first', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getBody().innerHTML,
      '<p>a</p>' +
      '<p>b</p>' +
      '<p><br data-mce-bogus="1"></p>'
    );
  });

  suite.test('TestCase-TBA: Lists: Handle several empty unordered list items without error', function (editor) {
    editor.getBody().innerHTML = (
      '<ul>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li></li>' +
      '<li>c</li>' +
      '<li></li>' +
      '<li>d</li>' +
      '<li></li>' +
      '<li>e</li>' +
      '</ul>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'li:first', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getBody().innerHTML,
      '<p>a</p>' +
      '<p>b</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>c</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>d</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>e</p>'
    );
  });

  suite.test('TestCase-TBA: Lists: Handle one empty ordered list items without error', function (editor) {
    editor.getBody().innerHTML = (
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li></li>' +
      '</ol>'
    );

    editor.execCommand('SelectAll');
    LegacyUnit.setSelection(editor, 'li:first', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getBody().innerHTML,
      '<p>a</p>' +
      '<p>b</p>' +
      '<p><br data-mce-bogus="1"></p>'
    );
  });

  suite.test('TestCase-TBA: Lists: Handle several empty ordered list items without error', function (editor) {
    editor.getBody().innerHTML = (
      '<ol>' +
      '<li>a</li>' +
      '<li>b</li>' +
      '<li></li>' +
      '<li>c</li>' +
      '<li></li>' +
      '<li>d</li>' +
      '<li></li>' +
      '<li>e</li>' +
      '</ol>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'li:first', 0, 'li:last', 0);
    LegacyUnit.execCommand(editor, 'InsertOrderedList');

    LegacyUnit.equal(editor.getBody().innerHTML,
      '<p>a</p>' +
      '<p>b</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>c</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>d</p>' +
      '<p><br data-mce-bogus=\"1\"></p>' +
      '<p>e</p>'
    );
  });

  suite.test('TestCase-TBA: Lists: Apply list on paragraphs with list between', function (editor) {
    editor.getBody().innerHTML = (
      '<p>a</p>' +
      '<ol>' +
      '<li>b</li>' +
      '</ol>' +
      '<p>c</p>'
    );

    editor.execCommand('SelectAll');
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');
    LegacyUnit.equal(editor.getBody().innerHTML, '<ul><li>a</li></ul><ol><li>b</li></ol><ul><li>c</li></ul>');
  });

  suite.test('TestCase-TBA: Lists: Apply unordered list on children on a fully selected ordered list', function (editor) {
    editor.getBody().innerHTML = (
      '<ol>' +
        '<li>a' +
          '<ol>' +
            '<li>b</li>' +
          '</ol>' +
        '</li>' +
        '<li>c</li>' +
      '</ol>'
    );

    editor.execCommand('SelectAll');
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');
    LegacyUnit.equal(editor.getBody().innerHTML, '<ul><li>a<ul><li>b</li></ul></li><li>c</li></ul>');
  });

  suite.test('TestCase-TBA: Lists: Apply unordered list on empty table cell', function (editor) {
    editor.getBody().innerHTML = (
      '<table>' +
        '<tbody>' +
          '<tr>' +
            '<td>' +
              '<br />' +
            '</td>' +
          '</tr>' +
        '</tbody>' +
      '</table>'
    );

    const rng = editor.dom.createRng();
    rng.setStart(editor.dom.select('td')[0], 0);
    rng.setEnd(editor.dom.select('td')[0], 1);
    editor.selection.setRng(rng);

    LegacyUnit.execCommand(editor, 'InsertUnorderedList');
    LegacyUnit.equal(editor.getBody().innerHTML, '<table><tbody><tr><td><ul><li><br></li></ul></td></tr></tbody></table>');
  });

  suite.test('TestCase-TBA: Lists: Apply unordered list on table cell with two lines br', function (editor) {
    editor.getBody().innerHTML = (
      '<table>' +
        '<tbody>' +
          '<tr>' +
            '<td>' +
              'a<br>b' +
            '</td>' +
          '</tr>' +
        '</tbody>' +
      '</table>'
    );

    const rng = editor.dom.createRng();
    rng.setStart(editor.dom.select('td')[0].firstChild, 0);
    rng.setEnd(editor.dom.select('td')[0].firstChild, 0);
    editor.selection.setRng(rng);

    LegacyUnit.execCommand(editor, 'InsertUnorderedList');
    LegacyUnit.equal(editor.getBody().innerHTML, '<table><tbody><tr><td><ul><li>a</li></ul>b</td></tr></tbody></table>');
  });

  suite.test('TestCase-TBA: Lists: Apply UL list to single P with forced_root_block_attrs', function (editor) {
    editor.settings.forced_root_block = 'p';
    editor.settings.forced_root_block_attrs = {
      'data-editor': '1'
    };

    editor.getBody().innerHTML = LegacyUnit.trimBrs(
      '<p data-editor="1">a</p>'
    );

    editor.focus();
    LegacyUnit.setSelection(editor, 'p', 0);
    LegacyUnit.execCommand(editor, 'InsertUnorderedList');

    LegacyUnit.equal(editor.getContent(), '<ul><li data-editor="1">a</li></ul>');
    LegacyUnit.equal(editor.selection.getNode().nodeName, 'LI');

    editor.settings.forced_root_block = 'p';
    delete editor.settings.forced_root_block_attrs;
  });

  TinyLoader.setupLight(function (editor, onSuccess, onFailure) {
    Pipeline.async({}, Log.steps('TBA', 'Lists: Apply list tests', suite.toSteps(editor)), onSuccess, onFailure);
  }, {
    plugins: 'lists',
    add_unload_trigger: false,
    disable_nodechange: true,
    indent: false,
    entities: 'raw',
    valid_elements:
      'li[style|class|data-custom|data-custom1|data-custom2],ol[style|class|data-custom|data-custom1|data-custom2],' +
      'ul[style|class|data-custom|data-custom1|data-custom2],dl,dt,dd,em,strong,span,#p,div,br',
    valid_styles: {
      '*': 'color,font-size,font-family,background-color,font-weight,' +
        'font-style,text-decoration,float,margin,margin-top,margin-right,' +
        'margin-bottom,margin-left,display,position,top,left,list-style-type'
    },
    theme: 'silver',
    base_url: '/project/tinymce/js/tinymce'
  }, success, failure);
});
