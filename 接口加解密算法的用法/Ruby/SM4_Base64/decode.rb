
# encoding: utf-8
# author:{"补天"=>"等闲却变故人心"}

require 'sinatra'
require 'openssl'
require 'base64'

def sm4_encrypt(key, iv, plaintext)
  cipher = OpenSSL::Cipher.new('sm4-cbc')
  cipher.encrypt
  cipher.key = key
  cipher.iv = iv
  encrypted = cipher.update(plaintext) + cipher.final
  Base64.strict_encode64(encrypted)
end

# SM4 解密方法
def sm4_decrypt(key, iv, ciphertext)
  cipher = OpenSSL::Cipher.new('sm4-cbc')
  cipher.decrypt
  cipher.key = key
  cipher.iv = iv
  decrypted = cipher.update(Base64.strict_decode64(ciphertext)) + cipher.final
  decrypted.force_encoding('utf-8')
end

post '/encode' do
  key = 'oibnskaxcde@rsf!'
  iv = 'oibnskaxcde@rsf!'
  param = params[:dataBody].strip
  p param
  ciphertext = sm4_encrypt(key, iv, param)
  p ciphertext
  return ciphertext
end

post '/decode' do
  key = 'oibnskaxcde@rsf!'
  iv = 'oibnskaxcde@rsf!'
  param = params[:dataBody].strip
  p param
  plaintext = sm4_decrypt(key, iv, param)
  p plaintext
  return plaintext
end

set :bind, '0.0.0.0'
set :port, 8889
