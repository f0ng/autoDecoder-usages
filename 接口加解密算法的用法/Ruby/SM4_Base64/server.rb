
# encoding: utf-8
# author:{"补天"=>"等闲却变故人心"}
require 'openssl'
require 'base64'
require 'sinatra'
require 'mysql2'

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



post '/test' do
  begin
    key = 'oibnskaxcde@rsf!'
    iv = 'oibnskaxcde@rsf!'
    param = request.body.read.strip
    p param
    decryptedtext = sm4_decrypt(key, iv, param)
    p decryptedtext
    id = JSON.parse(decryptedtext)['id']
    p id
    client = Mysql2::Client.new(
      :host     => '127.0.0.1', # 主机
      :username => 'root',      # 用户名
      :password => 'root',    # 密码
      :database => 'security',      # 数据库
      :encoding => 'utf8'       # 编码
    )
    results = client.query("SELECT * FROM users WHERE id = #{id}")
    client.close
    result_hash = results.first
    p result_hash
    result_json = JSON.parse(result_hash.to_json)['username']
    p result_json
    #return param
    plaintext = sm4_encrypt(key, iv, result_json.to_s)
    return plaintext
  rescue => e
    puts e.message
    puts e.backtrace.inspect
    return ""
  end
end

set :bind, '0.0.0.0'
set :port, 8899

key = 'oibnskaxcde@rsf!'
iv = 'oibnskaxcde@rsf!'
plaintext = '{"id":"1"}'
#plaintext = JSON.parse(plaintext)
p plaintext
# 加密明文
ciphertext = sm4_encrypt(key, iv, plaintext)
puts ("加密："+ciphertext)


# 解密密文
#decryptedtext = sm4_decrypt(key, iv, ciphertext)
#puts ("解密结果："+ decryptedtext)
