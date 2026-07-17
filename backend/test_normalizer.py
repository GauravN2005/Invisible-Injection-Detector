from app.normalization.normalizer import InputNormalizer


sample = """
Hello\u200B

**ChatGPT**

Visit &lt;b&gt;OpenAI&lt;/b&gt;

"""

print(InputNormalizer.normalize(sample))